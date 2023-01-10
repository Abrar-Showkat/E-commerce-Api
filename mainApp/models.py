from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_delete, pre_delete

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, firstname=None, lastname=None, phone=None, password=None):
        if not username:
            ValueError('Users must have an username')
        user = self.model(username=username, email=email, firstname=firstname,
                          lastname=lastname, phone=phone, is_admin=False)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):

        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=30)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    is_admin = models.BooleanField(default=False, blank=True)
    is_staff = models.BooleanField(default=True)
    otp_counter = models.IntegerField(default=0)
    last_login = None

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    User = models.Manager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


class Address(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, name='address')
    city = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=20, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.address.username + " 's" + ' Adress'

    class Meta:
        verbose_name_plural = 'Addresses'


class Category(models.Model):
    # id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20)
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product')

    description = models.TextField()
    image = models.ImageField(
        upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.product_name


def delete_parent(sender, instance, **kwargs):
    if instance.address:
        instance.address.delete()


pre_delete.connect(delete_parent, sender=User)

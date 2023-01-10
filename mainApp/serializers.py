from rest_framework import serializers
from .models import User, Address, Category, Product
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class AddressSerializer(serializers.ModelSerializer):
    class Meta:

        model = Address
        fields = ['city', 'street', 'number', 'zipcode']


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    email = serializers.EmailField(max_length=20, required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all(), message='This email already exists')])

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User
        fields = ['email', 'username', 'password',
                  'firstname', 'lastname', 'phone', 'address', ]

    def create(self, validated_data):
        print(validated_data)
        address_data = validated_data.pop('address')
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Address.objects.create(address=user, **address_data)

        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        # instance.password = validated_data.get('password', instance.password)

        instance.firstname = validated_data.get(
            'firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.set_password(instance.password)
        instance.save()

        address.city = address_data.get('city', address.city)
        address.street = address_data.get('street', address.street)
        address.number = address_data.get('number', address.number)
        address.zipcode = address_data.get('zipcode', address.zipcode)
        address.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(validators=[UniqueValidator(
        Category.objects.all(), message='This Category Already Exists')])

    class Meta:

        model = Category
        fields = ['id', 'category_name']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image',  'product_category']

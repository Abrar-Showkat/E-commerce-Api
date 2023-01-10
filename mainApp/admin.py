from django.contrib import admin
from .models import User, Address, Category, Product

# Register your models here.


class AddressAdmin(admin.ModelAdmin):

    fields = ('address', ('city', 'street'),
              ('number', 'zipcode'))


class AddressInline(admin.TabularInline):

    model = Address
    can_delete = False


class UserAdmin(admin.ModelAdmin):

    inlines = [AddressInline]


class ProductInline(admin.TabularInline):

    model = Product
    can_delete = False


# class SubCategoryInline(admin.TabularInline):

#     model = SubCategory

#     can_delete = False


class CategoryAdmin(admin.ModelAdmin):

    inlines = [ProductInline]


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)

# Generated by Django 3.2.5 on 2022-09-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20220903_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='product_price',
        ),
    ]

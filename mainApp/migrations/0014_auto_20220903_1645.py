# Generated by Django 3.2.5 on 2022-09-03 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_alter_subcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'SubCategory'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]

# Generated by Django 3.2.5 on 2022-12-05 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_auto_20221205_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mainApp.category'),
        ),
    ]

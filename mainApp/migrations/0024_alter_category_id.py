# Generated by Django 3.2.5 on 2023-01-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_auto_20230103_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.2.5 on 2022-11-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_auto_20220904_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_count',
            field=models.IntegerField(default=0),
        ),
    ]

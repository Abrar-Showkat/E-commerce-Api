# Generated by Django 3.2.5 on 2022-08-13 13:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('is_admin', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('zipcode', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=10)),
                ('lon', models.CharField(max_length=10)),
                ('Address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.user')),
            ],
        ),
    ]

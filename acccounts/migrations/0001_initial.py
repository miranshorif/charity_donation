# Generated by Django 4.2.4 on 2023-08-11 17:09

import acccounts.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', acccounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DonaterAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=180)),
                ('city', models.CharField(max_length=180)),
                ('postal_code', models.IntegerField()),
                ('country', models.CharField(max_length=180)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='acccounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Donater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField(unique=True)),
                ('image', models.ImageField(upload_to='midea/images')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='donater', to='acccounts.user')),
            ],
        ),
    ]

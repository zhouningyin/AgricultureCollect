# Generated by Django 3.2.5 on 2021-08-19 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_passward_users_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
    ]

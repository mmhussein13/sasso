# Generated by Django 4.2.16 on 2024-11-12 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_image',
        ),
    ]

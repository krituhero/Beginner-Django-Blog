# Generated by Django 4.0.3 on 2023-02-11 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopdata', '0007_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
# Generated by Django 4.0.3 on 2023-01-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
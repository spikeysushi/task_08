# Generated by Django 2.1.5 on 2020-01-29 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='pic',
            new_name='logo',
        ),
    ]

# Generated by Django 2.2.20 on 2021-08-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_merge_20210816_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]

# Generated by Django 2.2.20 on 2021-08-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20210816_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]

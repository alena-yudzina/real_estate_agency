# Generated by Django 2.2.20 on 2021-08-12 16:28
import phonenumbers
from django.db import migrations


def fill_pure_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phone):
            flat.owner_pure_phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = ''
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210812_1736'),
    ]

    operations = [
        migrations.RunPython(fill_pure_phone_number, move_backward),
    ]

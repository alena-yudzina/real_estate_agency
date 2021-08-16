# Generated by Django 2.2.20 on 2021-08-16 08:00

from django.db import migrations


def fill_owners_data(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for owner in Owner.objects.all():
        flat = Flat.objects.filter(owner=owner.owner).first()
        owner.owners_phonenumber = flat.owners_phonenumber
        owner.owner_pure_phone = flat.owner_pure_phone
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210816_1050'),
    ]

    operations = [
        migrations.RunPython(fill_owners_data)
    ]

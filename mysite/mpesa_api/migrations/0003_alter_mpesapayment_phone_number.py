# Generated by Django 3.2.8 on 2021-10-21 17:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0002_auto_20211020_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]

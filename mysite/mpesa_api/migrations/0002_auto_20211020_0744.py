# Generated by Django 3.2.8 on 2021-10-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaCallBacks',
        ),
        migrations.DeleteModel(
            name='MpesaCalls',
        ),
        migrations.AlterModelOptions(
            name='mpesapayment',
            options={},
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='organization_balance',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='type',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='full_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

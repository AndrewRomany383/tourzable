# Generated by Django 4.2.4 on 2023-08-19 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_account_visa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='visa',
        ),
    ]

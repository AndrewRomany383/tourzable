# Generated by Django 4.2.4 on 2023-08-19 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_visa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='visa',
        ),
    ]

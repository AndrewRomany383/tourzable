# Generated by Django 4.2.4 on 2023-08-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_remember_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='language',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='client_user/'),
        ),
    ]
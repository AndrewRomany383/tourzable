# Generated by Django 4.2.4 on 2023-10-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_reviews_delete_tripreview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TripBook',
        ),
    ]
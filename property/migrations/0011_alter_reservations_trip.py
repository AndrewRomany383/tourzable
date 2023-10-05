# Generated by Django 4.2.4 on 2023-09-29 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_reservations_client_alter_reservations_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_trips', to='property.trip'),
        ),
    ]

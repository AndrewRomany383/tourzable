# Generated by Django 4.2.4 on 2023-10-01 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0013_alter_reservations_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]

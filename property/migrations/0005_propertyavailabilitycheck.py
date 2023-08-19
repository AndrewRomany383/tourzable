# Generated by Django 4.2.4 on 2023-08-18 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_alter_property_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAvailabilityCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel_name', models.CharField(max_length=100)),
                ('check_in', models.DateField(default=django.utils.timezone.now)),
                ('check_out', models.DateField(default=django.utils.timezone.now)),
                ('adults_number', models.PositiveIntegerField(default=0)),
                ('children_number', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquery_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

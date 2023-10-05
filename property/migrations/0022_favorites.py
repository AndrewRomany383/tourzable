# Generated by Django 4.2.4 on 2023-10-04 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0021_alter_reviews_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_favorites', to=settings.AUTH_USER_MODEL)),
                ('favs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_favorites', to='property.trip')),
            ],
            options={
                'verbose_name_plural': 'Favorites',
            },
        ),
    ]
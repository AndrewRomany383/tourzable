# Generated by Django 4.2.4 on 2023-10-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_alter_tripreview_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripreview',
            name='rate',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='rate'),
        ),
    ]
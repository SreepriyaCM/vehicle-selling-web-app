# Generated by Django 5.0 on 2023-12-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_remove_vehicles_price_remove_vehicles_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='best_selling',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

# Generated by Django 5.0 on 2023-12-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_rename_user_orders_user_orders_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='rating',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]

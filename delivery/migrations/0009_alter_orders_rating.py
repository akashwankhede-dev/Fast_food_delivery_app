# Generated by Django 5.0 on 2023-12-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_alter_orders_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

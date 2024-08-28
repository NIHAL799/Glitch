# Generated by Django 4.2.13 on 2024-08-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_discounted_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='max_price',
        ),
        migrations.AddField(
            model_name='products',
            name='is_offer_available',
            field=models.BooleanField(default=False),
        ),
    ]

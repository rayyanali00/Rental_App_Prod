# Generated by Django 3.2.7 on 2021-11-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_order_ordered_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_checkout',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

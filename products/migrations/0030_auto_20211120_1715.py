# Generated by Django 3.2.7 on 2021-11-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20211120_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, to='products.Cart'),
        ),
    ]

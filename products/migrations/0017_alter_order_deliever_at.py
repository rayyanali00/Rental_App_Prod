# Generated by Django 3.2.7 on 2021-11-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_order_deliever_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliever_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
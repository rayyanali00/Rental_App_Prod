# Generated by Django 3.2.7 on 2021-12-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_alter_order_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_accepted',
            field=models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accept'), ('reject', 'Reject')], default='Pending', max_length=30),
        ),
    ]

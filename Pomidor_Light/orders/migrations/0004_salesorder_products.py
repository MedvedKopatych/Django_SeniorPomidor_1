# Generated by Django 3.2.8 on 2021-10-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0003_auto_20211012_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]

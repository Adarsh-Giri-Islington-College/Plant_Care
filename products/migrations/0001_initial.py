# Generated by Django 5.0.2 on 2024-03-03 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_description', models.TextField()),
                ('added_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]

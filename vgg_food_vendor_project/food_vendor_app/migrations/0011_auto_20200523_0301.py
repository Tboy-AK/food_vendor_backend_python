# Generated by Django 3.0.6 on 2020-05-23 02:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_vendor_app', '0010_auto_20200523_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='frequencyOfReocurrence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None),
        ),
    ]

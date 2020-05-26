# Generated by Django 3.0.6 on 2020-05-16 17:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('dateTimeModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('phoneNumber', models.CharField(max_length=16, unique=True)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('dateTimeModified', models.DateTimeField(auto_now=True)),
                ('auth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Auth')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('isRecurring', models.BooleanField()),
                ('frequencyOfReocurrence', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MessageStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=16, unique=True)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('dateTimeModified', models.DateTimeField(auto_now=True)),
                ('auth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Auth')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('itemsOrdered', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('amountDue', models.CharField(max_length=50)),
                ('amountPaid', models.CharField(max_length=50)),
                ('amountOutstanding', models.CharField(max_length=50)),
                ('dateAndTimeOfOrder', models.DateTimeField(auto_now_add=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Customer')),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Menu')),
                ('orderStatusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.OrderStatus')),
                ('vendorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('fromVendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Vendor')),
                ('messageStatusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.MessageStatus')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Order')),
                ('toCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='vendorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_vendor_app.Vendor'),
        ),
    ]
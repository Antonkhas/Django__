# Generated by Django 4.1.7 on 2023-03-30 10:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('tg_id', models.BigIntegerField()),
                ('tg_username', models.CharField(max_length=50)),
                ('custom_shipping_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TicketsSupport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecom.users')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('total_price', models.FloatField(default=0.0)),
                ('payment_status', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecom.users')),
            ],
        ),
        migrations.CreateModel(
            name='AccumulativePoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecom.users')),
            ],
        ),
    ]
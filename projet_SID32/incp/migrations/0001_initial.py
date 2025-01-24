# Generated by Django 5.1.5 on 2025-01-19 23:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_measure', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
                ('moughataa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commune_set', to='incp.moughataa')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('type', models.CharField(choices=[('supermarket', 'Supermarché'), ('market', 'Marché'), ('shop', 'Boutique'), ('other', 'Autre')], max_length=50)),
                ('gps_lat', models.FloatField(default=0.0)),
                ('gps_lon', models.FloatField(default=0.0)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incp.commune')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weighting', models.DecimalField(decimal_places=2, help_text='Pondération du produit dans le panier (en %)', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_products', to='incp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_products', to='incp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_from', models.CharField(default='01/01/2000', max_length=10)),
                ('date_to', models.CharField(default='31/12/2099', max_length=10)),
                ('point_of_sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_prices', to='incp.pointofsale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prices', to='incp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='incp.producttype'),
        ),
        migrations.AddField(
            model_name='moughataa',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='moughataa_set', to='incp.wilaya'),
        ),
    ]

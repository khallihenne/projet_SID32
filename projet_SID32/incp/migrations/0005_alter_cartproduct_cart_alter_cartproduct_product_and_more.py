# Generated by Django 4.2.18 on 2025-02-03 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incp', '0004_alter_productprice_date_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='incp.cart'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='incp.product'),
        ),
        migrations.AlterField(
            model_name='commune',
            name='moughataa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commune_set', to='incp.moughataa'),
        ),
        migrations.AlterField(
            model_name='moughataa',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moughataa_set', to='incp.wilaya'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='incp.producttype'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='point_of_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='incp.pointofsale'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='incp.product'),
        ),
    ]

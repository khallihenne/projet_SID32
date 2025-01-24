from django.db import migrations
from datetime import datetime

def convert_dates(apps, schema_editor):
    ProductPrice = apps.get_model('incp', 'ProductPrice')
    for price in ProductPrice.objects.all():
        # Convertir date_from
        try:
            date_from = datetime.strptime(price.date_from, '%d/%m/%Y').date()
            price.date_from = date_from
        except ValueError:
            price.date_from = '2000-01-01'
        
        # Convertir date_to
        try:
            date_to = datetime.strptime(price.date_to, '%d/%m/%Y').date()
            price.date_to = date_to
        except ValueError:
            price.date_to = '2099-12-31'
        
        price.save()

class Migration(migrations.Migration):

    dependencies = [
        ('incp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(convert_dates),
    ]

from django.core.management.base import BaseCommand
import pandas as pd
import os
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Génère des fichiers Excel exemple pour l\'importation des données'

    def handle(self, *args, **options):
        # Créer le dossier sample_files s'il n'existe pas
        output_dir = 'sample_files'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Exemple pour Wilaya
        wilaya_data = {
            'code': ['W01', 'W02', 'W03'],
            'name': ['Nouakchott', 'Nouadhibou', 'Kiffa']
        }
        pd.DataFrame(wilaya_data).to_excel(f'{output_dir}/wilaya_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier wilaya_example.xlsx créé'))

        # Exemple pour Moughataa
        moughataa_data = {
            'code': ['M01', 'M02', 'M03'],
            'label': ['Tevragh Zeina', 'Ksar', 'Teyarett'],
            'wilaya_code': ['W01', 'W01', 'W01']
        }
        pd.DataFrame(moughataa_data).to_excel(f'{output_dir}/moughataa_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier moughataa_example.xlsx créé'))

        # Exemple pour Commune
        commune_data = {
            'code': ['C01', 'C02', 'C03'],
            'name': ['Commune 1', 'Commune 2', 'Commune 3'],
            'moughataa_code': ['M01', 'M01', 'M02']
        }
        pd.DataFrame(commune_data).to_excel(f'{output_dir}/commune_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier commune_example.xlsx créé'))

        # Exemple pour ProductType
        product_type_data = {
            'code': ['PT01', 'PT02', 'PT03'],
            'label': ['Céréales', 'Légumes', 'Fruits'],
            'description': ['Produits céréaliers', 'Légumes frais', 'Fruits frais']
        }
        pd.DataFrame(product_type_data).to_excel(f'{output_dir}/product_type_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_type_example.xlsx créé'))

        # Exemple pour Product
        product_data = {
            'code': ['P01', 'P02', 'P03'],
            'name': ['Riz', 'Tomates', 'Pommes'],
            'description': ['Riz blanc', 'Tomates fraîches', 'Pommes rouges'],
            'unit_measure': ['kg', 'kg', 'kg'],
            'product_type_code': ['PT01', 'PT02', 'PT03']
        }
        pd.DataFrame(product_data).to_excel(f'{output_dir}/product_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_example.xlsx créé'))

        # Exemple pour PointOfSale
        point_of_sale_data = {
            'code': ['POS01', 'POS02', 'POS03'],
            'type': ['supermarket', 'market', 'shop'],
            'gps_lat': [18.0735, 18.0865, 18.0923],
            'gps_lon': [-15.9582, -15.9785, -15.9654],
            'commune_code': ['C01', 'C02', 'C03']
        }
        pd.DataFrame(point_of_sale_data).to_excel(f'{output_dir}/point_of_sale_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier point_of_sale_example.xlsx créé'))

        # Exemple pour ProductPrice
        today = datetime.now()
        product_price_data = {
            'product_code': ['P01', 'P02', 'P03'],
            'point_of_sale_code': ['POS01', 'POS02', 'POS03'],
            'value': [350, 45, 120],
            'date_from': [(today - timedelta(days=30)).strftime('%d/%m/%Y')] * 3,
            'date_to': [today.strftime('%d/%m/%Y')] * 3
        }
        pd.DataFrame(product_price_data).to_excel(f'{output_dir}/product_price_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_price_example.xlsx créé'))

        # Exemple pour Cart
        cart_data = {
            'code': ['C01', 'C02', 'C03'],
            'name': ['Panier de base', 'Panier familial', 'Panier économique'],
            'description': ['Panier des produits de base', 'Panier pour famille', 'Panier à prix réduit']
        }
        pd.DataFrame(cart_data).to_excel(f'{output_dir}/cart_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier cart_example.xlsx créé'))

        # Exemple pour CartProduct
        cart_product_data = {
            'cart_code': ['C01', 'C01', 'C02'],
            'product_code': ['P01', 'P02', 'P03'],
            'weighting': [40, 30, 30],
            'date_from': [(today - timedelta(days=30)).strftime('%Y-%m-%d')] * 3,
            'date_to': [today.strftime('%Y-%m-%d')] * 3
        }
        pd.DataFrame(cart_product_data).to_excel(f'{output_dir}/cart_product_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier cart_product_example.xlsx créé'))

        self.stdout.write(self.style.SUCCESS('\nTous les fichiers exemple ont été créés dans le dossier "sample_files"'))

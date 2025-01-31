from django.core.management.base import BaseCommand
import pandas as pd
import os
from datetime import datetime, timedelta
import random

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
            'code': ['PT01', 'PT02', 'PT03', 'PT04', 'PT05'],
            'label': ['Céréales', 'Légumes', 'Fruits', 'Viandes', 'Produits laitiers'],
            'description': ['Produits céréaliers', 'Légumes frais', 'Fruits frais', 'Viandes fraîches', 'Produits laitiers frais']
        }
        pd.DataFrame(product_type_data).to_excel(f'{output_dir}/product_type_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_type_example.xlsx créé'))

        # Exemple pour Product avec plus de produits
        product_data = {
            'code': ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08'],
            'name': ['Riz', 'Tomates', 'Pommes', 'Viande bovine', 'Lait', 'Pain', 'Poulet', 'Oignons'],
            'description': ['Riz blanc', 'Tomates fraîches', 'Pommes rouges', 'Viande bovine fraîche', 'Lait frais', 'Pain traditionnel', 'Poulet entier', 'Oignons frais'],
            'unit_measure': ['kg', 'kg', 'kg', 'kg', 'L', 'kg', 'kg', 'kg'],
            'product_type_code': ['PT01', 'PT02', 'PT03', 'PT04', 'PT05', 'PT01', 'PT04', 'PT02']
        }
        pd.DataFrame(product_data).to_excel(f'{output_dir}/product_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_example.xlsx créé'))

        # Exemple pour PointOfSale avec plus de points de vente
        point_of_sale_data = {
            'code': ['POS01', 'POS02', 'POS03', 'POS04', 'POS05'],
            'type': ['supermarket', 'market', 'shop', 'supermarket', 'market'],
            'gps_lat': [18.0735, 18.0865, 18.0923, 18.1023, 18.0654],
            'gps_lon': [-15.9582, -15.9785, -15.9654, -15.9854, -15.9723],
            'commune_code': ['C01', 'C02', 'C03', 'C01', 'C02']
        }
        pd.DataFrame(point_of_sale_data).to_excel(f'{output_dir}/point_of_sale_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier point_of_sale_example.xlsx créé'))

        # Exemple pour ProductPrice avec données de 2019 à 2024
        product_codes = product_data['code']
        pos_codes = point_of_sale_data['code']
        
        price_data = []
        base_prices = {
            'P01': 300,  # Riz
            'P02': 40,   # Tomates
            'P03': 100,  # Pommes
            'P04': 800,  # Viande bovine
            'P05': 50,   # Lait
            'P06': 150,  # Pain
            'P07': 450,  # Poulet
            'P08': 35,   # Oignons
        }

        # Générer des prix pour chaque année de 2019 à 2024
        for year in range(2019, 2025):
            for month in range(1, 13):
                start_date = f'{year}-{month:02d}-01'
                end_date = f'{year}-{month:02d}-{"28" if month == 2 else "30" if month in [4,6,9,11] else "31"}'
                
                for product_code in product_codes:
                    base_price = base_prices[product_code]
                    for pos_code in pos_codes:
                        # Ajouter une variation aléatoire au prix de base (+/- 10%)
                        variation = random.uniform(-0.1, 0.1)
                        # Ajouter une augmentation progressive des prix (3% par an)
                        yearly_increase = 1 + (0.03 * (year - 2019))
                        price = round(base_price * (1 + variation) * yearly_increase, 2)
                        
                        price_data.append({
                            'product_code': product_code,
                            'point_of_sale_code': pos_code,
                            'value': price,
                            'date_from': start_date,
                            'date_to': end_date
                        })

        pd.DataFrame(price_data).to_excel(f'{output_dir}/product_price_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier product_price_example.xlsx créé'))

        # Exemple pour Cart avec plus de paniers
        cart_data = {
            'code': ['C01', 'C02', 'C03'],
            'name': ['Panier de base', 'Panier familial', 'Panier économique'],
            'description': ['Panier des produits de base', 'Panier pour famille', 'Panier à prix réduit']
        }
        pd.DataFrame(cart_data).to_excel(f'{output_dir}/cart_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier cart_example.xlsx créé'))

        # Exemple pour CartProduct avec pondérations réalistes
        cart_product_data = []
        weightings = {
            'C01': [  # Panier de base
                ('P01', 25),  # Riz
                ('P02', 15),  # Tomates
                ('P04', 20),  # Viande
                ('P05', 15),  # Lait
                ('P06', 25),  # Pain
            ],
            'C02': [  # Panier familial
                ('P01', 20),  # Riz
                ('P02', 10),  # Tomates
                ('P03', 10),  # Pommes
                ('P04', 15),  # Viande
                ('P05', 15),  # Lait
                ('P06', 15),  # Pain
                ('P07', 15),  # Poulet
            ],
            'C03': [  # Panier économique
                ('P01', 30),  # Riz
                ('P02', 20),  # Tomates
                ('P06', 30),  # Pain
                ('P08', 20),  # Oignons
            ]
        }

        for cart_code, products in weightings.items():
            for product_code, weight in products:
                cart_product_data.append({
                    'cart_code': cart_code,
                    'product_code': product_code,
                    'weighting': weight,
                    'date_from': '2019-01-01',
                    'date_to': '2024-12-31'
                })

        pd.DataFrame(cart_product_data).to_excel(f'{output_dir}/cart_product_example.xlsx', index=False)
        self.stdout.write(self.style.SUCCESS('Fichier cart_product_example.xlsx créé'))

        self.stdout.write(self.style.SUCCESS('\nTous les fichiers exemple ont été créés dans le dossier "sample_files"'))

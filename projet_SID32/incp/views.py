from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from .models import (
    Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, ProductPrice, Cart, CartProduct,
)
from datetime import datetime
from django.core.exceptions import ValidationError
from .forms import CartProductForm, ProductFilterForm, INPCCalculForm   # Importer le formulaire CartProductForm et ProductFilterForm
from django.db.models import Avg
from django.db.models.functions import Extract
from dateutil.relativedelta import relativedelta
import pandas as pd
from openpyxl import Workbook
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder

# --- VUES POUR Wilaya ---
class WilayaListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Wilaya
    template_name = "wilaya/wilaya_liste.html"


class WilayaCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    

class WilayaModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    

class WilayaSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Wilaya
    template_name = "wilaya/wilaya_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    


# --- VUES POUR Moughataa ---
class MoughataaListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Moughataa
    template_name = "moughataa/moughataa_liste.html"

class MoughataaCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas

class MoughataaModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas

class MoughataaSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Moughataa
    template_name = "moughataa/moughataa_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas


# --- VUES POUR Commune ---
class CommuneListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Commune
    template_name = "commune/commune_liste.html"

class CommuneCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 


class CommuneModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 

class CommuneSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Commune
    template_name = "commune/commune_confirmer_suppression.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 


# --- VUES POUR ProductType ---
class ProductTypeListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = ProductType
    template_name = "type_de_produit/type_de_produit_liste.html"

class ProductTypeCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('product_type_liste')

class ProductTypeModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('product_type_liste')

class ProductTypeSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = ProductType
    template_name = "type_de_produit/type_de_produit_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('product_type_liste')


# --- VUES POUR Product ---
class ProductListeView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Product
    template_name = "produit/produit_liste.html"
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        product_type_id = self.request.GET.get('product_type')
        
        if product_type_id:
            queryset = queryset.filter(product_type_id=product_type_id)
        
        return queryset.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductFilterForm(self.request.GET)
        return context

class ProductCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produit_liste')

class ProductModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('produit_liste')

class ProductSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Product
    template_name = "produit/produit_confirmer_suppression.html"
    def get_success_url(self):
        return reverse_lazy('produit_liste')


# --- VUES POUR PointOfSale ---
class PointOfSaleListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = PointOfSale
    template_name = "point_de_vente/point_de_vente_liste.html"

class PointOfSaleCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 

class PointOfSaleModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 

class PointOfSaleSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = PointOfSale
    template_name = "point_de_vente/point_de_vente_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 


# --- VUES POUR ProductPrice ---
class ProductPriceListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = ProductPrice
    template_name = "prix_de_produit/prix_de_produit_liste.html"
    context_object_name = 'prix_de_produits'

from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import ProductPrice

class ProductPriceCreerView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = ProductPrice
    fields = ['product', 'point_of_sale', 'value', 'date_from', 'date_to']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('prix_de_produit_liste')

    def form_valid(self, form):
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')

        # Assurer que les dates sont bien au format `dd/MM/YYYY`
        if isinstance(date_from, str):
            date_from = datetime.strptime(date_from, '%d/%m/%Y').date()

        if isinstance(date_to, str):
            date_to = datetime.strptime(date_to, '%d/%m/%Y').date()

        if date_from > date_to:
            form.add_error('date_to', "La date de fin doit être postérieure à la date de début.")
            return self.form_invalid(form)

        form.instance.date_from = date_from
        form.instance.date_to = date_to

        return super().form_valid(form)


class ProductPriceModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = ProductPrice
    fields = ['product', 'point_of_sale', 'value', 'date_from', 'date_to']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('prix_de_produit_liste')

    # def form_valid(self, form):
    #     # Valider les dates avant de sauvegarder
    #     date_from = form.cleaned_data.get('date_from')
    #     date_to = form.cleaned_data.get('date_to')

    #     try:
    #         date_from_obj = datetime.strptime(date_from, '%d/%m/%Y')
    #         date_to_obj = datetime.strptime(date_to, '%d/%m/%Y')
    #     except ValueError:
    #         form.add_error('date_from', "La date doit être au format DD/MM/YYYY.")
    #         return self.form_invalid(form)

    #     if date_from_obj > date_to_obj:
    #         form.add_error('date_to', "La date de fin doit être postérieure à la date de début.")
    #         return self.form_invalid(form)

    #     return super().form_valid(form)

class ProductPriceSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = ProductPrice
    
    template_name = "prix_de_produit/prix_de_produit_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('prix_de_produit_liste')


# --- VUES POUR Cart ---
class CartListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Cart
    template_name = "panier/panier_liste.html"
    context_object_name = 'object_list'
    ordering = ['name']

class CartCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')

class CartModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')

class CartSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Cart
    template_name = "panier/panier_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')


# --- VUES POUR CartProduct ---
class CartProductListeView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_liste.html"
    context_object_name = 'object_list'
    ordering = ['cart__name', 'product__name']

class CartProductCreerView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = CartProduct
    form_class = CartProductForm
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produit_de_panier_liste')

class CartProductModifierView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = CartProduct
    form_class = CartProductForm
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produit_de_panier_liste')

class CartProductSupprimerView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('produit_de_panier_liste')
    

#  page home:
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Avg
from django.db.models.functions import Extract

@login_required(login_url='login')
def home(request):
    # Obtenir la date actuelle
    current_date = datetime.now()
    
    # Liste pour stocker les INPC des 4 derniers mois
    last_months_inpc = []
    
    # Pour chacun des 4 derniers mois
    for i in range(4):
        # Calculer la date du mois
        date = current_date - relativedelta(months=i)
        year = date.year
        month = date.month
        
        # Récupérer les prix de l'année de base (2019)
        base_prices = ProductPrice.objects.filter(
            date_from__year=2019,
            date_from__month=month
        ).select_related('product', 'product__product_type')
        
        # Récupérer les prix du mois actuel
        current_prices = ProductPrice.objects.filter(
            date_from__year=year,
            date_from__month=month
        ).select_related('product', 'product__product_type')
        
        # Calculer l'INPC global
        product_types = ProductType.objects.all()
        total_weight = 0
        weighted_sum = 0
        
        for product_type in product_types:
            # Prix moyens pour ce type de produit
            base_avg = base_prices.filter(
                product__product_type=product_type
            ).aggregate(avg_price=Avg('value'))['avg_price'] or 0
            
            current_avg = current_prices.filter(
                product__product_type=product_type
            ).aggregate(avg_price=Avg('value'))['avg_price'] or 0
            
            # Calculer l'indice pour ce type
            if base_avg > 0:
                index = (current_avg / base_avg) * 100
            else:
                index = 0
                
            # Récupérer le poids total des produits de ce type
            products = CartProduct.objects.filter(
                product__product_type=product_type
            )
            type_weight = sum(cp.weighting for cp in products)
            total_weight += type_weight
            weighted_sum += index * type_weight
        
        # Calculer l'INPC global pour ce mois
        global_inpc = round(weighted_sum / total_weight if total_weight > 0 else 0, 2)
        
        # Ajouter à la liste
        last_months_inpc.append({
            'month': date.strftime('%B %Y'),
            'inpc': global_inpc
        })

    # Données pour le Line Chart : Évolution des prix moyens des produits de base
    products = Product.objects.filter(code__in=['P01', 'P02', 'P06'])  # Riz, Tomates, Pain
    price_data = {}
    labels = []
    
    for year in range(2019, 2025):
        for month in range(1, 13):
            date = f"{year}-{month:02d}"
            if date not in labels:
                labels.append(date)
    
    for product in products:
        prices = []
        for date in labels:
            year, month = date.split('-')
            avg_price = ProductPrice.objects.filter(
                product=product,
                date_from__year=year,
                date_from__month=month
            ).aggregate(Avg('value'))['value__avg'] or 0
            prices.append(round(avg_price, 2))
        price_data[product.name] = prices

    # Données pour le Pie Chart : Répartition des types de points de vente
    pos_types = PointOfSale.objects.values('type').annotate(
        count=Count('id')
    )
    pos_labels = [item['type'] for item in pos_types]
    pos_data = [item['count'] for item in pos_types]

    # Données pour le Bar Chart : Nombre de produits par type
    product_types = ProductType.objects.annotate(product_count=models.Count('products'))
    type_labels = [pt.label for pt in product_types]
    type_data = [pt.product_count for pt in product_types]

    # Calcul de l'INPC pour les 4 derniers mois
    current_date = datetime.now()
    last_months = []
    for i in range(4):
        month = current_date.month - i
        year = current_date.year
        if month <= 0:
            month += 12
            year -= 1
        last_months.append({
            'month': f"{year}-{month:02d}",
            'inpc': calculate_inpc_for_month(year, month)
        })

    # Données pour le graphique linéaire (évolution des prix)
    basic_products = ['Riz', 'Tomates', 'Pain']
    price_data = {}
    labels = []
    
    # Générer les dates de 2019 à 2024
    for year in range(2019, 2025):
        for month in range(1, 13):
            labels.append(f"{year}-{month:02d}")
    
    # Récupérer les prix moyens pour chaque produit
    for product_name in basic_products:
        product = Product.objects.filter(name=product_name).first()
        if product:
            prices = []
            for date_str in labels:
                year, month = map(int, date_str.split('-'))
                avg_price = ProductPrice.objects.filter(
                    product=product,
                    date_from__year=year,
                    date_from__month=month
                ).aggregate(avg_price=Avg('value'))['avg_price'] or 0
                prices.append(float(avg_price))
            price_data[product_name] = prices

    # Préparer les données pour le graphique linéaire en format JSON
    datasets = []
    for product_name, prices in price_data.items():
        datasets.append({
            'label': product_name,
            'data': prices,
            'fill': False,
            'tension': 0.1
        })
    price_data_json = json.dumps(datasets, cls=DjangoJSONEncoder)

    # Données pour le graphique circulaire (types de points de vente)
    pos_types = PointOfSale.objects.values('type').annotate(count=models.Count('id'))
    pos_labels = [pos['type'] for pos in pos_types]
    pos_data = [pos['count'] for pos in pos_types]

    # Données pour le graphique à barres (produits par catégorie)
    product_types = ProductType.objects.annotate(product_count=models.Count('products'))
    type_labels = [pt.label for pt in product_types]
    type_data = [pt.product_count for pt in product_types]

    context = {
        'last_months_inpc': last_months_inpc,
        'labels': json.dumps(labels),
        'price_data_json': price_data_json,
        'pos_labels': json.dumps(pos_labels),
        'pos_data': json.dumps(pos_data),
        'type_labels': json.dumps(type_labels),
        'type_data': json.dumps(type_data),
    }
    
    return render(request, 'home.html', context)

def calculate_inpc_for_month(year, month):
    """
    Calcule l'INPC pour un mois et une année donnés
    Base 100 en 2019
    """
    try:
        # Calculer la moyenne des prix pour ce mois
        current_prices = ProductPrice.objects.filter(
            date_from__year=year,
            date_from__month=month
        ).values('product').annotate(avg_price=Avg('value'))

        # Calculer la moyenne des prix pour 2019 (année de base)
        base_prices = ProductPrice.objects.filter(
            date_from__year=2019,
            date_from__month=month
        ).values('product').annotate(avg_price=Avg('value'))

        # Convertir en dictionnaires pour un accès plus facile
        current_dict = {p['product']: p['avg_price'] for p in current_prices if p['avg_price']}
        base_dict = {p['product']: p['avg_price'] for p in base_prices if p['avg_price']}

        # Calculer l'INPC uniquement pour les produits qui ont des prix dans les deux périodes
        common_products = set(current_dict.keys()) & set(base_dict.keys())
        
        if not common_products:
            return 0

        # Calculer la somme des variations relatives
        total_variation = sum(
            (current_dict[pid] / base_dict[pid]) * 100
            for pid in common_products
        )

        # Calculer la moyenne (INPC)
        inpc = total_variation / len(common_products)
        
        return round(inpc, 2)
    except Exception as e:
        print(f"Erreur dans le calcul de l'INPC pour {month}/{year}: {str(e)}")
        return 0

@login_required(login_url='login')
def wilaya_liste(request):
    # Logique pour afficher la liste des wilayas
    return render(request, 'wilaya/wilaya_liste.html')
@login_required(login_url='login')
def moughataa_liste(request):
    # Logique pour afficher la liste des moughataas
    return render(request, 'moughataa/moughataa_liste.html')
@login_required(login_url='login')
def commune_liste(request):
    # Logique pour afficher la liste des communes
    return render(request, 'commune/commune_liste.html')
@login_required(login_url='login')
def product_type_liste(request):
    # Logique pour afficher la liste des types de produit
    return render(request, 'type_de_produit/type_de_produit_liste.html')
@login_required(login_url='login')
def produit_liste(request):
    # Logique pour afficher la liste des produits
    return render(request, 'produit/produit_liste.html')
@login_required(login_url='login')
def point_of_sale_liste(request):
    # Logique pour afficher la liste des points de vente
    return render(request, 'point_de_vente/point_de_vente_liste.html')
@login_required(login_url='login')
def prix_de_produit_liste(request):
    # Logique pour afficher la liste des prix des produits
    return render(request, 'prix_de_produit/prix_de_produit_liste.html')
@login_required(login_url='login')
def panier_liste(request):
    # Logique pour afficher la liste des paniers
    return render(request, 'panier/panier_liste.html')
@login_required(login_url='login')
def produit_de_panier_liste(request):
    # Logique pour afficher la liste des produits dans le panier
    return render(request, 'produit_de_panier/panier_liste.html')


 # import 
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ExcelImportForm
# import pandas as pd
# from .models import (
#     ProductType, Product, Wilaya, Moughataa, Commune, 
#     PointOfSale, ProductPrice, Cart, CartProduct
# )
# from datetime import datetime
# @login_required(login_url='login')
# def excel_import(request):
#     if request.method == 'POST':
#         form = ExcelImportForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = form.cleaned_data['file']
#             model_type = form.cleaned_data['model_type']

#             try:
#                 # Lire le fichier Excel
#                 df = pd.read_excel(uploaded_file)

#                 # Méthodes d'importation pour chaque modèle
#                 import_methods = {
#                     'product_type': import_product_types,
#                     'product': import_products,
#                     'wilaya': import_wilayas,
#                     # 'moughataa': import_moughataa,
#                     'commune': import_communes,
#                     'point_of_sale': import_points_of_sale,
#                     'product_price': import_product_prices,
#                     'cart': import_carts,
#                     'cart_product': import_cart_products
#                 }

#                 # Appeler la méthode d'importation appropriée
#                 import_method = import_methods.get(model_type)
#                 if import_method:
#                     import_method(df)
#                     messages.success(request, f'Importation de {model_type} réussie!')
#                 else:
#                     messages.error(request, 'Type de modèle non reconnu')

#             except Exception as e:
#                 messages.error(request, f'Erreur lors de l\'importation: {str(e)}')

#             return redirect('import_export')  # Redirige vers la page d'import/export après succès
#     else:
#         form = ExcelImportForm()

#     return render(request, 'import/excel_import.html', {'form': form})

# # Méthodes d'importation pour chaque modèle
# @login_required(login_url='login')
# def import_product_types(df):
#     for _, row in df.iterrows():
#         ProductType.objects.create(
#             code=row['code'],
#             label=row['label'],
#             description=row.get('description', '')  # Optionnel
#         )
# @login_required(login_url='login')
# def import_products(df):
#     for _, row in df.iterrows():
#         product_type = ProductType.objects.get(code=row['product_type_code'])
#         Product.objects.create(
#             code=row['code'],
#             name=row['name'],
#             description=row.get('description', ''),  # Optionnel
#             unit_measure=row['unit_measure'],
#             product_type=product_type
#         )

# ... (ajoutez les autres méthodes d'importation ici)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
from openpyxl import Workbook
from datetime import datetime
from django.views.generic import TemplateView

class ImportExportView(LoginRequiredMixin,TemplateView):
    login_url = 'login'
    template_name = "import_export/import_export.html"
@login_required(login_url='login')
def import_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        model_type = request.POST.get('model_type')
        excel_file = request.FILES['file']
        
        try:
            # Vérifier que le fichier est un fichier Excel
            if not excel_file.name.endswith(('.xlsx', '.xls')):
                messages.error(request, 'Le fichier doit être au format Excel (.xlsx ou .xls).')
                return redirect('import_export')

            df = pd.read_excel(excel_file)
            print("Colonnes du fichier importé :", df.columns)
            print("Contenu du DataFrame :", df.head())

            # Vérifiez les colonnes requises en fonction du type de modèle
            required_columns = {
                'wilaya': ['code', 'name'],
                'moughataa': ['code', 'label', 'wilaya_code'],
                'commune': ['code', 'name', 'moughataa_code'],
                'product_type': ['code', 'label'],
                'product': ['code', 'name', 'unit_measure', 'product_type_code'],
                'point_of_sale': ['code', 'type', 'gps_lat', 'gps_lon', 'commune_code'],
                'product_price': ['product_code', 'point_of_sale_code', 'date_from', 'value'],
                'cart': ['code', 'name'],
                'cart_product': ['cart_code', 'product_code', 'date_from', 'weighting', 'date_to'],
            }

            if model_type in required_columns:
                missing_columns = [col for col in required_columns[model_type] if col not in df.columns]
                if missing_columns:
                    messages.error(request, f"Colonnes manquantes dans le fichier: {', '.join(missing_columns)}")
                    return redirect('import_export')

            # Appel de la fonction d'importation appropriée
            if model_type == 'wilaya':
                import_wilayas(df)
            elif model_type == 'moughataa':
                import_moughataas(df)
            elif model_type == 'commune':
                import_communes(df)
            elif model_type == 'product_type':
                import_product_types(df)
            elif model_type == 'product':
                import_products(df)
            elif model_type == 'point_of_sale':
                import_points_of_sale(df)
            elif model_type == 'product_price':
                import_product_prices(df)
            elif model_type == 'cart':
                import_carts(df)
            elif model_type == 'cart_product':
                import_cart_products(df)

            messages.success(request, f'Import des données {model_type} réussi!')
        except Exception as e:
            messages.error(request, f'Erreur lors de l\'import: {str(e)}')

        return redirect('import_export')

    return redirect('import_export')

def import_wilayas(df):
    try:
        for _, row in df.iterrows():
            if pd.isna(row['code']) or pd.isna(row['name']):
                raise ValueError("Les colonnes 'code' et 'name' ne peuvent pas être vides")
                
            Wilaya.objects.update_or_create(
                code=str(row['code']).strip(),
                defaults={'name': str(row['name']).strip()}
            )
    except Exception as e:
        raise Exception(f"Erreur lors de l'import des wilayas: {str(e)}")
@login_required(login_url='login')
def export_data(request):
    if request.method == 'POST':
        model_type = request.POST.get('model_type')
        
        try:
            if model_type == 'wilaya':
                df = export_wilayas()
            elif model_type == 'moughataa':
                df = export_moughataas()
            elif model_type == 'commune':
                df = export_communes()
            elif model_type == 'product_type':
                df = export_product_types()
            elif model_type == 'product':
                df = export_products()
            elif model_type == 'point_of_sale':
                df = export_points_of_sale()
            elif model_type == 'product_price':
                df = export_product_prices()
            elif model_type == 'cart':
                df = export_carts()
            elif model_type == 'cart_product':
                df = export_cart_products()
            
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{model_type}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx"'
            
            df.to_excel(response, index=False)
            return response
            
        except Exception as e:
            messages.error(request, f'Erreur lors de l\'export: {str(e)}')
            return redirect('import_export')
    
    return redirect('import_export')

# Fonctions d'import pour chaque modèle

def import_moughataas(df):
    for _, row in df.iterrows():
        wilaya = Wilaya.objects.get(code=row['wilaya_code'])
        Moughataa.objects.update_or_create(
            code=row['code'],
            defaults={
                'label': row['label'],
                'wilaya': wilaya
            }
        )

def import_communes(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['moughataa_code', 'code', 'name']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        moughataa = Moughataa.objects.get(code=row['moughataa_code'])
        Commune.objects.update_or_create(
            code=row['code'],
            defaults={
                'name': row['name'],
                'moughataa': moughataa
            }
        )

def import_product_types(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['code', 'label']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        ProductType.objects.update_or_create(
            code=row['code'],
            defaults={
                'label': row['label'],
                'description': row.get('description', '')
            }
        )

def import_products(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['product_type_code', 'code', 'name', 'unit_measure']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        product_type = ProductType.objects.get(code=row['product_type_code'])
        Product.objects.update_or_create(
            code=row['code'],
            defaults={
                'name': row['name'],
                'description': row.get('description', ''),
                'unit_measure': row['unit_measure'],
                'product_type': product_type
            }
        )

def import_points_of_sale(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['commune_code', 'code', 'type', 'gps_lat', 'gps_lon']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        commune = Commune.objects.get(code=row['commune_code'])
        PointOfSale.objects.update_or_create(
            code=row['code'],
            defaults={
                'type': row['type'],
                'gps_lat': row['gps_lat'],
                'gps_lon': row['gps_lon'],
                'commune': commune
            }
        )

def import_product_prices(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['product_code', 'point_of_sale_code', 'date_from', 'value']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        product = Product.objects.get(code=row['product_code'])
        point_of_sale = PointOfSale.objects.get(code=row['point_of_sale_code'])
        ProductPrice.objects.update_or_create(
            product=product,
            point_of_sale=point_of_sale,
            date_from=row['date_from'],
            defaults={
                'value': row['value'],
                'date_to': row['date_to']
            }
        )

def import_carts(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['code', 'name']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        Cart.objects.update_or_create(
            code=row['code'],
            defaults={
                'name': row['name'],
                'description': row.get('description', '')
            }
        )

def import_cart_products(df):
    # Vérifier si les colonnes nécessaires existent dans le DataFrame
    required_columns = ['cart_code', 'product_code', 'date_from', 'weighting', 'date_to']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"La colonne '{column}' est manquante dans le DataFrame.")

    for _, row in df.iterrows():
        cart = Cart.objects.get(code=row['cart_code'])
        product = Product.objects.get(code=row['product_code'])
        CartProduct.objects.update_or_create(
            cart=cart,
            product=product,
            date_from=row['date_from'],
            defaults={
                'weighting': row['weighting'],
                'date_to': row['date_to']
            }
        )

# Fonctions d'export pour chaque modèle
@login_required(login_url='login')
def export_wilayas():
    wilayas = Wilaya.objects.all()
    data = [{'code': w.code, 'name': w.name} for w in wilayas]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_moughataas():
    moughataas = Moughataa.objects.all()
    data = [{
        'code': m.code,
        'label': m.label,
        'wilaya_code': m.wilaya.code
    } for m in moughataas]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_communes():
    communes = Commune.objects.all()
    data = [{
        'code': c.code,
        'name': c.name,
        'moughataa_code': c.moughataa.code
    } for c in communes]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_product_types():
    product_types = ProductType.objects.all()
    data = [{
        'code': pt.code,
        'label': pt.label,
        'description': pt.description
    } for pt in product_types]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_products():
    products = Product.objects.all()
    data = [{
        'code': p.code,
        'name': p.name,
        'description': p.description,
        'unit_measure': p.unit_measure,
        'product_type_code': p.product_type.code
    } for p in products]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_points_of_sale():
    points = PointOfSale.objects.all()
    data = [{
        'code': p.code,
        'type': p.type,
        'gps_lat': p.gps_lat,
        'gps_lon': p.gps_lon,
        'commune_code': p.commune.code
    } for p in points]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_product_prices():
    prices = ProductPrice.objects.all()
    data = [{
        'product_code': p.product.code,
        'point_of_sale_code': p.point_of_sale.code,
        'value': p.value,
        'date_from': p.date_from,
        'date_to': p.date_to
    } for p in prices]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_carts():
    carts = Cart.objects.all()
    data = [{
        'code': c.code,
        'name': c.name,
        'description': c.description
    } for c in carts]
    return pd.DataFrame(data)
@login_required(login_url='login')
def export_cart_products():
    cart_products = CartProduct.objects.all()
    data = [{
        'cart_code': cp.cart.code,
        'product_code': cp.product.code,
        'weighting': cp.weighting,
        'date_from': cp.date_from,
        'date_to': cp.date_to
    } for cp in cart_products]
    return pd.DataFrame(data)

@login_required(login_url='login')
def calculate_inpc(request):
    form = INPCCalculForm(request.GET if request.GET else None)
    context = {'form': form}
    
    if form.is_valid():
        selected_year = form.cleaned_data['year']
        selected_month = int(form.cleaned_data['month'])
        
        # Récupérer les prix de l'année de base (2019) pour le même mois
        base_prices = ProductPrice.objects.annotate(
            month=Extract('date_from', 'month'),
            year=Extract('date_from', 'year')
        ).filter(
            year=2019,
            month=selected_month
        ).select_related('product', 'product__product_type')
        
        # Récupérer les prix de l'année sélectionnée pour le même mois
        current_prices = ProductPrice.objects.annotate(
            month=Extract('date_from', 'month'),
            year=Extract('date_from', 'year')
        ).filter(
            year=selected_year,
            month=selected_month
        ).select_related('product', 'product__product_type')
        
        # Calculer l'INPC par type de produit
        product_types = ProductType.objects.all()
        inpc_by_type = []
        total_weight = 0
        weighted_sum = 0
        
        for product_type in product_types:
            # Prix moyens pour ce type de produit
            base_avg = base_prices.filter(
                product__product_type=product_type
            ).aggregate(avg_price=Avg('value'))['avg_price'] or 0
            
            current_avg = current_prices.filter(
                product__product_type=product_type
            ).aggregate(avg_price=Avg('value'))['avg_price'] or 0
            
            # Calculer l'indice pour ce type
            if base_avg > 0:
                index = (current_avg / base_avg) * 100
            else:
                index = 0
                
            # Récupérer le poids total des produits de ce type
            products = CartProduct.objects.filter(
                product__product_type=product_type
            )
            type_weight = sum(cp.weighting for cp in products)
            total_weight += type_weight
            weighted_sum += index * type_weight
            
            inpc_by_type.append({
                'type': product_type.label,
                'base_price': round(base_avg, 2),
                'current_price': round(current_avg, 2),
                'index': round(index, 2),
                'weight': round(type_weight, 2)
            })
        
        # Calculer l'INPC global
        global_inpc = round(weighted_sum / total_weight if total_weight > 0 else 0, 2)
        
        context.update({
            'inpc_by_type': inpc_by_type,
            'global_inpc': global_inpc,
            'selected_year': selected_year,
            'selected_month': dict(INPCCalculForm.MONTH_CHOICES)[int(selected_month)],
            'has_results': True
        })
    
    return render(request, 'inpc/calculate_inpc.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie!')
            return redirect('home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'auth/login.html')
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté.')
    return redirect('login')


# chart

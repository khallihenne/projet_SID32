from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, ProductPrice, Cart, CartProduct
)

# --- VUES POUR Wilaya ---
class WilayaListeView(ListView):
    model = Wilaya
    template_name = "wilaya/wilaya_liste.html"


class WilayaCreerView(CreateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    

class WilayaModifierView(UpdateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    

class WilayaSupprimerView(DeleteView):
    model = Wilaya
    template_name = "wilaya/wilaya_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('wilaya_liste')  # Redirige vers la liste des wilayas
    


# --- VUES POUR Moughataa ---
class MoughataaListeView(ListView):
    model = Moughataa
    template_name = "moughataa/moughataa_liste.html"

class MoughataaCreerView(CreateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas

class MoughataaModifierView(UpdateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas

class MoughataaSupprimerView(DeleteView):
    model = Moughataa
    template_name = "moughataa/moughataa_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('moughataa_liste')  # Redirige vers la liste des moughataas


# --- VUES POUR Commune ---
class CommuneListeView(ListView):
    model = Commune
    template_name = "commune/commune_liste.html"

class CommuneCreerView(CreateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 


class CommuneModifierView(UpdateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 

class CommuneSupprimerView(DeleteView):
    model = Commune
    template_name = "commune/commune_confirmer_suppression.html"
    def get_success_url(self):
        return reverse_lazy('commune_liste') 


# --- VUES POUR ProductType ---
class ProductTypeListeView(ListView):
    model = ProductType
    template_name = "type_de_produit/type_de_produit_liste.html"

class ProductTypeCreerView(CreateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('product_type_liste')

class ProductTypeModifierView(UpdateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('product_type_liste')

class ProductTypeSupprimerView(DeleteView):
    model = ProductType
    template_name = "type_de_produit/type_de_produit_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('product_type_liste')


# --- VUES POUR Product ---
class ProductListeView(ListView):
    model = Product
    template_name = "produit/produit_liste.html"

class ProductCreerView(CreateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produit_liste')

class ProductModifierView(UpdateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"
    def get_success_url(self):
        return reverse_lazy('produit_liste')

class ProductSupprimerView(DeleteView):
    model = Product
    template_name = "produit/produit_confirmer_suppression.html"
    def get_success_url(self):
        return reverse_lazy('produit_liste')


# --- VUES POUR PointOfSale ---
class PointOfSaleListeView(ListView):
    model = PointOfSale
    template_name = "point_de_vente/point_de_vente_liste.html"

class PointOfSaleCreerView(CreateView):
    model = PointOfSale
    fields = ['name', 'code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 

class PointOfSaleModifierView(UpdateView):
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 

class PointOfSaleSupprimerView(DeleteView):
    model = PointOfSale
    template_name = "point_de_vente/point_de_vente_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('point_of_sale_liste') 


# --- VUES POUR ProductPrice ---
class ProductPriceListeView(ListView):
    model = ProductPrice
    template_name = "prix_de_produit/prix_de_produit_liste.html"

class ProductPriceCreerView(CreateView):
    model = ProductPrice
    fields = ['product', 'point_of_sale', 'value', 'date_from', 'date_to']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('prixdeproduit_list') 
    

class ProductPriceModifierView(UpdateView):
    model = ProductPrice
    fields = ['product', 'point_of_sale', 'value', 'date_from', 'date_to']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('prixdeproduit_list') 

class ProductPriceSupprimerView(DeleteView):
    model = ProductPrice
    template_name = "prix_de_produit/prix_de_produit_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('prixdeproduit_list') 


# --- VUES POUR Cart ---
class CartListeView(ListView):
    model = Cart
    template_name = "panier/panier_liste.html"

class CartCreerView(CreateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')

class CartModifierView(UpdateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')

class CartSupprimerView(DeleteView):
    model = Cart
    template_name = "panier/panier_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')


# --- VUES POUR CartProduct ---
class CartProductListeView(ListView):
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_liste.html"

    def get_success_url(self):
        return reverse_lazy('panier_liste')

class CartProductCreerView(CreateView):
    model = CartProduct
    fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produitdepanier_list')

class CartProductModifierView(UpdateView):
    model = CartProduct
    fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"

    def get_success_url(self):
        return reverse_lazy('produitdepanier_list')

class CartProductSupprimerView(DeleteView):
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_confirmer_suppression.html"

    def get_success_url(self):
        return reverse_lazy('produitdepanier_list')

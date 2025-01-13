from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import (
    Wilaya, Moughataa, Commune, TypeDeProduit, Produit, PointDeVente, PrixDeProduit, Cart, CartProduct
)

# --- VUES POUR Wilaya ---
class WilayaListeView(LoginRequiredMixin, ListView):
    model = Wilaya
    template_name = "wilaya/wilaya_liste.html"   

class WilayaCreerView(LoginRequiredMixin, CreateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"
    success_url = reverse_lazy('wilaya_liste')

class WilayaModifierView(LoginRequiredMixin, UpdateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = "wilaya/wilaya_formulaire.html"
    success_url = reverse_lazy('wilaya_liste')

class WilayaSupprimerView(LoginRequiredMixin, DeleteView):
    model = Wilaya
    template_name = "wilaya/wilaya_confirmer_suppression.html"
    success_url = reverse_lazy('wilaya_liste')

# --- VUES POUR Moughataa ---
class MoughataaListeView(LoginRequiredMixin, ListView):
    model = Moughataa
    template_name = "moughataa/moughataa_liste.html"

class MoughataaCreerView(LoginRequiredMixin, CreateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"
    success_url = reverse_lazy('moughataa_liste')

class MoughataaModifierView(LoginRequiredMixin, UpdateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = "moughataa/moughataa_formulaire.html"
    success_url = reverse_lazy('moughataa_liste')

class MoughataaSupprimerView(LoginRequiredMixin, DeleteView):
    model = Moughataa
    template_name = "moughataa/moughataa_confirmer_suppression.html"
    success_url = reverse_lazy('moughataa_liste')

# --- VUES POUR Commune ---
class CommuneListeView(LoginRequiredMixin, ListView):
    model = Commune
    template_name = "commune/commune_liste.html"

class CommuneCreerView(LoginRequiredMixin, CreateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    success_url = reverse_lazy('commune_liste')

class CommuneModifierView(LoginRequiredMixin, UpdateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = "commune/commune_formulaire.html"
    success_url = reverse_lazy('commune_liste')

class CommuneSupprimerView(LoginRequiredMixin, DeleteView):
    model = Commune
    template_name = "commune/commune_confirmer_suppression.html"
    success_url = reverse_lazy('commune_liste')

# --- VUES POUR TypeDeProduit ---
class TypeDeProduitListeView(LoginRequiredMixin, ListView):
    model = TypeDeProduit
    template_name = "type_de_produit/type_de_produit_liste.html"

class TypeDeProduitCreerView(LoginRequiredMixin, CreateView):
    model = TypeDeProduit
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"
    success_url = reverse_lazy('type_de_produit_liste')

class TypeDeProduitModifierView(LoginRequiredMixin, UpdateView):
    model = TypeDeProduit
    fields = ['code', 'label', 'description']
    template_name = "type_de_produit/type_de_produit_formulaire.html"
    success_url = reverse_lazy('type_de_produit_liste')

class TypeDeProduitSupprimerView(LoginRequiredMixin, DeleteView):
    model = TypeDeProduit
    template_name = "type_de_produit/type_de_produit_confirmer_suppression.html"
    success_url = reverse_lazy('type_de_produit_liste')

# --- VUES POUR Produit ---
class ProduitListeView(LoginRequiredMixin, ListView):
    model = Produit
    template_name = "produit/produit_liste.html"

class ProduitCreerView(LoginRequiredMixin, CreateView):
    model = Produit
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"
    success_url = reverse_lazy('produit_liste')

class ProduitModifierView(LoginRequiredMixin, UpdateView):
    model = Produit
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = "produit/produit_formulaire.html"
    success_url = reverse_lazy('produit_liste')

class ProduitSupprimerView(LoginRequiredMixin, DeleteView):
    model = Produit
    template_name = "produit/produit_confirmer_suppression.html"
    success_url = reverse_lazy('produit_liste')

# --- VUES POUR PointDeVente ---
class PointDeVenteListeView(LoginRequiredMixin, ListView):
    model = PointDeVente
    template_name = "point_de_vente/point_de_vente_liste.html"

class PointDeVenteCreerView(LoginRequiredMixin, CreateView):
    model =PointDeVente
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"
    success_url = reverse_lazy('point_de_vente_liste')

class PointDeVenteModifierView(LoginRequiredMixin, UpdateView):
    model = PointDeVente
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = "point_de_vente/point_de_vente_formulaire.html"
    success_url = reverse_lazy('point_de_vente_liste')

class PointDeVenteSupprimerView(LoginRequiredMixin, DeleteView):
    model = PointDeVente
    template_name = "point_de_vente/point_de_vente_confirmer_suppression.html"
    success_url = reverse_lazy('point_de_vente_liste')

# --- VUES POUR PrixDeProduit ---
class PrixDeProduitListeView(LoginRequiredMixin, ListView):
    model = PrixDeProduit
    template_name = "prix_de_produit/prix_de_produit_liste.html"

class PrixDeProduitCreerView(LoginRequiredMixin, CreateView):
    model = PrixDeProduit
    fields = ['produit', 'prix']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"
    success_url = reverse_lazy('prix_de_produit_liste')

class PrixDeProduitModifierView(LoginRequiredMixin, UpdateView):
    model = PrixDeProduit
    fields = ['produit', 'prix']
    template_name = "prix_de_produit/prix_de_produit_formulaire.html"
    success_url = reverse_lazy('prix_de_produit_liste')

class PrixDeProduitSupprimerView(LoginRequiredMixin, DeleteView):
    model = PrixDeProduit
    template_name = "prix_de_produit/prix_de_produit_confirmer_suppression.html"
    success_url = reverse_lazy('prix_de_produit_liste')

# --- VUES POUR Panier ---
class PanierListeView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = "panier/panier_liste.html"

class PanierCreerView(LoginRequiredMixin, CreateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"
    success_url = reverse_lazy('panier_liste')

class PanierModifierView(LoginRequiredMixin, UpdateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = "panier/panier_formulaire.html"
    success_url = reverse_lazy('panier_liste')

class PanierSupprimerView(LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = "panier/panier_confirmer_suppression.html"
    success_url = reverse_lazy('panier_liste')

# --- VUES POUR ProduitDePanier ---
class ProduitDePanierListeView(LoginRequiredMixin, ListView):
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_liste.html"

class ProduitDePanierCreerView(LoginRequiredMixin, CreateView):
    model = CartProduct
    fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"
    success_url = reverse_lazy('produit_de_panier_liste')

class ProduitDePanierModifierView(LoginRequiredMixin, UpdateView):
    model = CartProduct
    fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']
    template_name = "produit_de_panier/produit_de_panier_formulaire.html"
    success_url = reverse_lazy('produit_de_panier_liste')

class ProduitDePanierSupprimerView(LoginRequiredMixin, DeleteView):
    model = CartProduct
    template_name = "produit_de_panier/produit_de_panier_confirmer_suppression.html"
    success_url = reverse_lazy('produit_de_panier_liste')

from django import forms
from .models import (
    Wilaya, Moughataa, Commune, ProduitType, Produit, PointDeVente, PrixDeProduit, Panier, ProduitDePanier
)

# Formulaire pour Wilaya
class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['name', 'region']

# Formulaire pour Moughataa
class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['name', 'wilaya']

# Formulaire pour Commune
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['name', 'moughataa']

# Formulaire pour ProduitType
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProduitType
        fields = ['name', 'description']

# Formulaire pour Produit
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['name', 'description', 'price', 'product_type', 'image']

# Formulaire pour PointDeVente
class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['name', 'location', 'contact']

# Formulaire pour PrixDeProduit
class PrixDeProduitForm(forms.ModelForm):
    class Meta:
        model = PrixDeProduit
        fields = ['produit', 'price']

# Formulaire pour Panier
class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['user', 'date_created']

# Formulaire pour ProduitDePanier
class ProduitDePanierForm(forms.ModelForm):
    class Meta:
        model = ProduitDePanier
        fields = ['panier', 'produit', 'quantity']

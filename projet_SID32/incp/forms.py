from django import forms
from django.forms.widgets import DateInput
from .models import (
    Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, ProductPrice, Cart, CartProduct
)

# Formulaire pour Wilaya
class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['code', 'name']

# Formulaire pour Moughataa
class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['code', 'label', 'wilaya']

# Formulaire pour Commune
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['code', 'name', 'moughataa']

# Formulaire pour ProductType
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['code', 'label', 'description']

# Formulaire pour Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'unit_measure', 'product_type']

# Formulaire pour PointOfSale
class PointOfSaleForm(forms.ModelForm):

    class Meta:
        model = PointOfSale
        fields = ['name', 'code', 'type', 'gps_lat', 'gps_lon', 'commune']
        

# Formulaire pour ProductPrice
class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['product', 'point_of_sale', 'value', 'date_from', 'date_to']
        widgets = {
            'date_from': forms.TextInput(attrs={'type': 'text', 'class': 'datepicker'}),
            'date_to': forms.TextInput(attrs={'type': 'text', 'class': 'datepicker'}),
        }

# Formulaire pour Cart
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['code', 'name', 'description']

# Formulaire pour CartProduct
class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']

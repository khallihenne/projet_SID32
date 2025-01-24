from django import forms
from django.forms.widgets import DateInput
from datetime import datetime
from django.core.exceptions import ValidationError
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
        fields = [ 'code', 'type', 'gps_lat', 'gps_lon', 'commune']
        

# Formulaire pour ProductPrice
class ProductPriceForm(forms.Form):
    valeur = forms.FloatField(label="Valeur")
    date_from = forms.CharField(label="Date de Début")
    date_to = forms.CharField(label="Date de Fin")
    produit = forms.CharField(label="Produit")
    point_of_sale = forms.CharField(label="Point de Vente")

    def clean_date_from(self):
        date_from = self.cleaned_data['date_from']
        try:
            datetime.strptime(date_from, '%d/%m/%Y')
        except ValueError:
            raise ValidationError("La date doit être au format DD/MM/YYYY.")
        return date_from

    def clean_date_to(self):
        date_to = self.cleaned_data['date_to']
        try:
            datetime.strptime(date_to, '%d/%m/%Y')
        except ValueError:
            raise ValidationError("La date doit être au format DD/MM/YYYY.")
        return date_to

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')

        if date_from and date_to:
            date_from_obj = datetime.strptime(date_from, '%d/%m/%Y')
            date_to_obj = datetime.strptime(date_to, '%d/%m/%Y')
            if date_from_obj > date_to_obj:
                raise ValidationError("La date de fin doit être postérieure à la date de début.")
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
        widgets = {
            'cart': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'weighting': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'step': '0.01',
                'required': True
            }),
            'date_from': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'date_to': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordonner les paniers par nom
        self.fields['cart'].queryset = Cart.objects.all().order_by('name')
        # Ordonner les produits par nom
        self.fields['product'].queryset = Product.objects.all().order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')

        if date_from and date_to and date_from > date_to:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")
        
        weighting = cleaned_data.get('weighting')
        if weighting is not None:
            if weighting < 0 or weighting > 100:
                raise ValidationError("La pondération doit être comprise entre 0 et 100.")

        return cleaned_data
    
class ExcelImportForm(forms.Form):
    MODEL_CHOICES = [
        ('product_type', 'Types de Produits'),
        ('product', 'Produits'),
        ('wilaya', 'Wilayas'),
        ('moughataa', 'Moughataa'),
        ('commune', 'Communes'),
        ('point_of_sale', 'Points de Vente'),
        ('product_price', 'Prix des Produits'),
        ('cart', 'Paniers'),
        ('cart_product', 'Produits des Paniers'),
    ]
    
    file = forms.FileField(
        label='Sélectionner un fichier Excel',
        help_text='Formats acceptés: .xlsx, .xls',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    model_type = forms.ChoiceField(
        label='Type de Données',
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class ProductFilterForm(forms.Form):
    product_type = forms.ModelChoiceField(
        queryset=ProductType.objects.all(),
        required=False,
        empty_label="Tous les types",
        label="Type de produit",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class INPCCalculForm(forms.Form):
    MONTH_CHOICES = [
        (1, 'Janvier'), (2, 'Février'), (3, 'Mars'),
        (4, 'Avril'), (5, 'Mai'), (6, 'Juin'),
        (7, 'Juillet'), (8, 'Août'), (9, 'Septembre'),
        (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')
    ]
    
    year = forms.IntegerField(
        label="Année",
        min_value=2019,
        max_value=2100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez l\'année'
        })
    )
    
    month = forms.ChoiceField(
        label="Mois",
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
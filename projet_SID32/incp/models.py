from django.db import models
from django.shortcuts import render


class Wilaya(models.Model):
    code = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Moughataa(models.Model):
    code = models.CharField(max_length=10, default='')
    label = models.CharField(max_length=255, default='')
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Commune(models.Model):
    code = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=255, default='')
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TypeDeProduit(models.Model):
    code = models.CharField(max_length=10, unique=True, default='')
    label = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.label

class Produit(models.Model):
    nom = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    type_de_produit = models.ForeignKey(TypeDeProduit, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class PointDeVente(models.Model):
    code = models.CharField(max_length=10, default='')
    type = models.CharField(max_length=50, default='')
    gps_lat = models.FloatField(default=0.0)
    gps_lon = models.FloatField(default=0.0)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.commune.name}"

class PrixDeProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Prix pour {self.produit.nom}"

class Cart(models.Model):
    code = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    weighting = models.FloatField(default=0.0)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.nom} - {self.cart.name}"

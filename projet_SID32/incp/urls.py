from django.urls import path
from .views import (
    WilayaListeView, WilayaCreerView, WilayaModifierView, WilayaSupprimerView,
    MoughataaListeView, MoughataaCreerView, MoughataaModifierView, MoughataaSupprimerView,
    CommuneListeView, CommuneCreerView, CommuneModifierView, CommuneSupprimerView,
    TypeDeProduitListeView, TypeDeProduitCreerView, TypeDeProduitModifierView, TypeDeProduitSupprimerView,
    ProduitListeView, ProduitCreerView, ProduitModifierView, ProduitSupprimerView,
    PointDeVenteListeView, PointDeVenteCreerView, PointDeVenteModifierView, PointDeVenteSupprimerView,
    PrixDeProduitListeView, PrixDeProduitCreerView, PrixDeProduitModifierView, PrixDeProduitSupprimerView,
    PanierListeView, PanierCreerView, PanierModifierView, PanierSupprimerView,
    ProduitDePanierListeView, ProduitDePanierCreerView, ProduitDePanierModifierView, ProduitDePanierSupprimerView
)

urlpatterns = [
    # Routes pour Wilaya
    path('wilaya/', WilayaListeView.as_view(), name='wilaya_liste'),
    path('wilaya/creer/', WilayaCreerView.as_view(), name='wilaya_creer'),
    path('wilaya/<int:pk>/modifier/', WilayaModifierView.as_view(), name='wilaya_modifier'),
    path('wilaya/<int:pk>/supprimer/', WilayaSupprimerView.as_view(), name='wilaya_supprimer'),

    # Routes pour Moughataa
    path('moughataa/', MoughataaListeView.as_view(), name='moughataa_liste'),
    path('moughataa/creer/', MoughataaCreerView.as_view(), name='moughataa_creer'),
    path('moughataa/<int:pk>/modifier/', MoughataaModifierView.as_view(), name='moughataa_modifier'),
    path('moughataa/<int:pk>/supprimer/', MoughataaSupprimerView.as_view(), name='moughataa_supprimer'),

    # Routes pour Commune
    path('commune/', CommuneListeView.as_view(), name='commune_liste'),
    path('commune/creer/', CommuneCreerView.as_view(), name='commune_creer'),
    path('commune/<int:pk>/modifier/', CommuneModifierView.as_view(), name='commune_modifier'),
    path('commune/<int:pk>/supprimer/', CommuneSupprimerView.as_view(), name='commune_supprimer'),

    # Routes pour TypeDeProduit
    path('type-de-produit/', TypeDeProduitListeView.as_view(), name='type_de_produit_liste'),
    path('type-de-produit/creer/', TypeDeProduitCreerView.as_view(), name='type_de_produit_creer'),
    path('type-de-produit/<int:pk>/modifier/', TypeDeProduitModifierView.as_view(), name='type_de_produit_modifier'),
    path('type-de-produit/<int:pk>/supprimer/', TypeDeProduitSupprimerView.as_view(), name='type_de_produit_supprimer'),

    # Routes pour Produit
    path('produit/', ProduitListeView.as_view(), name='produit_liste'),
    path('produit/creer/', ProduitCreerView.as_view(), name='produit_creer'),
    path('produit/<int:pk>/modifier/', ProduitModifierView.as_view(), name='produit_modifier'),
    path('produit/<int:pk>/supprimer/', ProduitSupprimerView.as_view(), name='produit_supprimer'),

    # Routes pour PointDeVente
    path('point-de-vente/', PointDeVenteListeView.as_view(), name='point_de_vente_liste'),
    path('point-de-vente/creer/', PointDeVenteCreerView.as_view(), name='point_de_vente_creer'),
    path('point-de-vente/<int:pk>/modifier/', PointDeVenteModifierView.as_view(), name='point_de_vente_modifier'),
    path('point-de-vente/<int:pk>/supprimer/', PointDeVenteSupprimerView.as_view(), name='point_de_vente_supprimer'),

    # Routes pour PrixDeProduit
    path('prix-de-produit/', PrixDeProduitListeView.as_view(), name='prix_de_produit_liste'),
    path('prix-de-produit/creer/', PrixDeProduitCreerView.as_view(), name='prix_de_produit_creer'),
    path('prix-de-produit/<int:pk>/modifier/', PrixDeProduitModifierView.as_view(), name='prix_de_produit_modifier'),
    path('prix-de-produit/<int:pk>/supprimer/', PrixDeProduitSupprimerView.as_view(), name='prix_de_produit_supprimer'),

    # Routes pour Panier
    path('panier/', PanierListeView.as_view(), name='panier_liste'),
    path('panier/creer/', PanierCreerView.as_view(), name='panier_creer'),
    path('panier/<int:pk>/modifier/', PanierModifierView.as_view(), name='panier_modifier'),
    path('panier/<int:pk>/supprimer/', PanierSupprimerView.as_view(), name='panier_supprimer'),

    # Routes pour ProduitDePanier
    path('produit-de-panier/', ProduitDePanierListeView.as_view(), name='produit_de_panier_liste'),
    path('produit-de-panier/creer/', ProduitDePanierCreerView.as_view(), name='produit_de_panier_creer'),
    path('produit-de-panier/<int:pk>/modifier/', ProduitDePanierModifierView.as_view(), name='produit_de_panier_modifier'),
    path('produit-de-panier/<int:pk>/supprimer/', ProduitDePanierSupprimerView.as_view(), name='produit_de_panier_supprimer'),
]

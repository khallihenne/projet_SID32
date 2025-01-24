from . import views
from django.urls import path
from .views import (
    WilayaListeView, WilayaCreerView, WilayaModifierView, WilayaSupprimerView,
    MoughataaListeView, MoughataaCreerView, MoughataaModifierView, MoughataaSupprimerView,
    CommuneListeView, CommuneCreerView, CommuneModifierView, CommuneSupprimerView,
    ProductTypeListeView, ProductTypeCreerView, ProductTypeModifierView, ProductTypeSupprimerView,
    ProductListeView, ProductCreerView, ProductModifierView, ProductSupprimerView,
    PointOfSaleListeView, PointOfSaleCreerView, PointOfSaleModifierView, PointOfSaleSupprimerView,
    ProductPriceListeView, ProductPriceCreerView, ProductPriceModifierView, ProductPriceSupprimerView,
    CartListeView, CartCreerView, CartModifierView, CartSupprimerView,
    CartProductSupprimerView, CartProductModifierView, CartProductCreerView, CartProductListeView,
    ImportExportView,
)
from django.contrib.auth import views as auth_views
urlpatterns = [
    # URLs d'authentification
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Routes pour Wilaya
    path('wilaya/', WilayaListeView.as_view(), name='wilaya_liste'),
    path('wilaya/creer/', WilayaCreerView.as_view(), name='wilaya_cree'),
    path('wilaya/<int:pk>/modifier/', WilayaModifierView.as_view(), name='wilaya_modifier'),
    path('wilaya/<int:pk>/supprimer/', WilayaSupprimerView.as_view(), name='wilaya_supprimer'),

    # Routes pour Moughataa
    path('moughataa/', MoughataaListeView.as_view(), name='moughataa_liste'),
    path('moughataa/creer/', MoughataaCreerView.as_view(), name='moughataa_create'),
    path('moughataa/<int:pk>/modifier/', MoughataaModifierView.as_view(), name='moughataa_modifier'),
    path('moughataa/<int:pk>/supprimer/', MoughataaSupprimerView.as_view(), name='moughataa_supprimer'),

    # Routes pour Commune
    path('commune/', CommuneListeView.as_view(), name='commune_liste'),
    path('commune/creer/', CommuneCreerView.as_view(), name='commune_create'),
    path('commune/<int:pk>/modifier/', CommuneModifierView.as_view(), name='commune_modifier'),
    path('commune/<int:pk>/supprimer/', CommuneSupprimerView.as_view(), name='commune_supprimer'),

    # Routes pour ProductType
    path('type-de-produit/', ProductTypeListeView.as_view(), name='product_type_liste'),
    path('type-de-produit/creer/', ProductTypeCreerView.as_view(), name='type_de_produit_create'),
    path('type-de-produit/<int:pk>/modifier/', ProductTypeModifierView.as_view(), name='type_de_produit_modifier'),
    path('type-de-produit/<int:pk>/supprimer/', ProductTypeSupprimerView.as_view(), name='type_de_produit_supprimer'),

    # Routes pour Product
    path('produit/', ProductListeView.as_view(), name='produit_liste'),
    path('produit/creer/', ProductCreerView.as_view(), name='produit_create'),
    path('produit/<int:pk>/modifier/', ProductModifierView.as_view(), name='produit_modifier'),
    path('produit/<int:pk>/supprimer/', ProductSupprimerView.as_view(), name='produit_supprimer'),
    #   of sale 
   path('point-de-vente/', PointOfSaleListeView.as_view(), name='point_of_sale_liste'),
   path('point-de-vente/creer/', PointOfSaleCreerView.as_view(), name='point_of_sale_create'),
   path('point-de-vente/<int:pk>/modifier/', PointOfSaleModifierView.as_view(), name='point_of_sale_modifier'),
   path('point-de-vente/<int:pk>/supprimer/', PointOfSaleSupprimerView.as_view(), name='point_of_sale_supprimer'),

    # Routes pour ProductPrice
    path('prix-de-produit/', ProductPriceListeView.as_view(), name='prix_de_produit_liste'),
    path('prix-de-produit/creer/', ProductPriceCreerView.as_view(), name='prix_de_produit_create'),
    path('prix-de-produit/<int:pk>/modifier/', ProductPriceModifierView.as_view(), name='prix_de_produit_update'),
    path('prix-de-produit/<int:pk>/supprimer/', ProductPriceSupprimerView.as_view(), name='prix_de_produit_delete'),

    # Routes pour Cart
    path('panier/', CartListeView.as_view(), name='panier_liste'),
    path('panier/creer/', CartCreerView.as_view(), name='panier_create'),
    path('panier/<int:pk>/modifier/', CartModifierView.as_view(), name='panier_update'),
    path('panier/<int:pk>/supprimer/', CartSupprimerView.as_view(), name='panier_delete'),
    
    # Routes pour CartProduct
    path('produit-de-panier/', CartProductListeView.as_view(), name='produit_de_panier_liste'),
    path('produit-de-panier/creer/', CartProductCreerView.as_view(), name='produit_de_panier_create'),
    path('produit-de-panier/<int:pk>/modifier/', CartProductModifierView.as_view(), name='produit_de_panier_update'),
    path('produit-de-panier/<int:pk>/supprimer/', CartProductSupprimerView.as_view(), name='produit_de_panier_delete'),

    #  Page d'accueil
    path('', views.home, name='home'),  # Page d'accueil
    path('wilaya/', views.wilaya_liste, name='wilaya_liste'),  # Page des wilayas
    path('moughataa/', views.moughataa_liste, name='moughataa_liste'),  # Page des moughataas
    path('commune/', views.commune_liste, name='commune_liste'),  # Page des communes
    path('type-de-produit/', views.product_type_liste, name='product_type_liste'),  # Page des types de produit
    path('produit/', views.produit_liste, name='produit_liste'),  # Page des produits
    path('point-de-vente/', views.point_of_sale_liste, name='point_of_sale_liste'),  # Page des points de vente
    path('prix-de-produit/', views.prix_de_produit_liste, name='prix_de_produit_liste'),  # Page des prix des produits
    path('panier/', views.panier_liste, name='panier_liste'),  # Page des paniers
    path('produit-de-panier/', views.produit_de_panier_liste, name='produit_de_panier_liste'),  # Page des produits dans le panier
    # Import/Export
    path('import-export/', ImportExportView.as_view(), name='import_export'),
    path('import-data/', views.import_data, name='import_data'),
    path('export-data/', views.export_data, name='export_data'),
    # path('import/', views.excel_import, name='excel_import'),
    path('inpc/calculate/', views.calculate_inpc, name='calculate_inpc'),
   ]
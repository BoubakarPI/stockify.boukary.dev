from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
   # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='ajouter_panier'),
   # path('panier/', views.panier, name='panier'),
    #path('finalize-order/', views.finalize_order, name='finalize_order'),
    path('commande/<int:commande_id>/', views.commande_detail, name='commande_detail'),
    path('ajouter_commande/', views.ajouter_commande, name='ajouter_commande'),
]

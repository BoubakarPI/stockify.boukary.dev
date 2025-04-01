from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('ajouter_commande/<int:product_id>/', views.ajouter_commande, name='ajouter_commande'),
    path('ajouter_commande/', views.ajouter_commande, name='ajouter_commande'),
  
]

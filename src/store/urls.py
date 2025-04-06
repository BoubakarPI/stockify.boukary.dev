from django.urls import path

from .views import product_list, product_detail, add_order

app_name = 'store'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_order/<int:product_id>/', add_order, name='add_order'),
    #path('add_order/', add_order, name='add_order'),

]
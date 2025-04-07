from django.urls import path

from .views import StoreListView, product_detail, add_order

app_name = 'store'
urlpatterns = [
    path('', StoreListView.as_view(), name='index'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_order/<int:product_id>/', add_order, name='add_order'),
    #path('add_order/', add_order, name='add_order'),

]
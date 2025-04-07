from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, validate_commande

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('orders', ProductListView.as_view(), name='orders'),
    path('activate-order/<int:order_id>', validate_commande, name='activate_order'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name="product_detail"),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]
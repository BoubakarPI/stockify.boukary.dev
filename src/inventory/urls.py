from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name="product"),
]
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
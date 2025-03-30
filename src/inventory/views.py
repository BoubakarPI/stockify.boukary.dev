from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"


class ProductDetailView(DetailView):
    template_name = 'inventory/product.html'
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs['slug'])

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product_content.html"


class ProductDetailView(DetailView):
    template_name = 'inventory/product.html'
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs['slug'])

# CRUD

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'stock', 'description', 'thumbnail']
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'stock', 'description', 'thumbnail']
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')
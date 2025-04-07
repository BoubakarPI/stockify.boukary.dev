from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from inventory.models import Product
from django.contrib import messages
from .forms import OrderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StoreListView(ListView):
    model = Product
    template_name = "store/product_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name", "").strip()
        stock = self.request.GET.get("stock", "").strip()

        if name:
            queryset = queryset.filter(name__icontains=name)

        if stock:
            try:
                stock = int(stock)
                queryset = queryset.filter(stock__gte=stock)
            except ValueError:
                pass  # Ignore les valeurs non numériques

        return queryset



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


def add_order(request, product_id=None):
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if product:
                order.product = product
            order.save()
            messages.success(request,
                             "Commande effectuée avec succès ! Vous pouvez commander à nouveau.")
            return redirect('/')
    else:
        form = OrderForm(initial={'product': product})

    return render(request, 'store/add_order.html', {'product': product})




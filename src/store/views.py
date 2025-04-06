from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import Product
from django.contrib import messages
from .forms import OrderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request):
    products = Product.objects.all()

    query = request.GET.get('search')
    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'store/product_list.html', {'products': products})


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




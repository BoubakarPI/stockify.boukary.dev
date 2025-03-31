from django.shortcuts import render, redirect,get_object_or_404
from .forms import  CommandeForm
from .models import Product, Commande,CommandeItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirecte vers la page panier après la soumission du formulaire
    context = {'form': form}
    return render(request, 'ajouter_commande.html', context)


def commande_detail(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    return render(request, 'commande_detail.html', {'commande': commande})

from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from django.contrib import messages
from .forms import CommandeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def product_list(request):
    products = Product.objects.all()

    # Gestion de la recherche
    query = request.GET.get('recherche')
    if query:
        products = products.filter(name__icontains=query)

    # Pagination
    paginator = Paginator(products, 3)  # 3 produits par page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)  # Si la page n'est pas un entier, afficher la première page
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Si la page est trop grande, afficher la dernière page

    return render(request, 'produit/product_list.html', {'products': products})




def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'produit/product_detail.html', {'product': product})


def ajouter_commande(request, product_id=None):
    produit = None
    if product_id:
        produit = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            if produit:
                commande.produit = produit  # Associer le produit
            commande.save()
            messages.success(request, "Commande effectuée avec succès ! Vous pouvez commander à nouveau.")  # ✅ Message de succès
            return redirect('/')  # Redirection vers la liste des commandes
    else:
        form = CommandeForm(initial={'produit': produit})

    return render(request, 'commande/ajouter_commande.html', {'form': form, 'produit': produit})




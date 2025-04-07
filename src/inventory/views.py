from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, ActivityLog
from store.models import Order

from stockify.middleware import min_role_required, RoleRequiredMixin

import logging

logger = logging.getLogger(__name__)


class ProductListView(ListView):
    model = Product
    template_name = "product_content.html"

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

class ProductDetailView(DetailView):
    template_name = 'inventory/product.html'
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs['slug'])

# CRUD

class ProductCreateView(RoleRequiredMixin, LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'stock', 'description', 'thumbnail']
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')
    login_url = '/accounts/signin/'
    required_role = 'editor'


    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors de l'ajout du produit. Vérifiez les champs et réessayez.")
        return redirect('products')

    def form_valid(self, form):
        response = super().form_valid(form)

        ActivityLog.objects.create(
            activity_id=f"LOG-{self.object.id}",
            user_email=self.request.user.email,
            user_fullname= self.request.user.fullname,
            ip_address=get_client_ip(self.request),
            action='add',
            object_type='Produit',
            object_id=str(self.object.id),
            object_name=self.object.name,
            changes= clean_json_values({
                "name": ["-", self.object.name],
                "price": ["-", self.object.price],
                "stock": ["-", self.object.stock],
                "description": ["-", self.object.description]
            }),
            message=f"Nouveau produit ajouté au catalogue par {self.request.user.fullname}"
        )

        return response


class ProductUpdateView(RoleRequiredMixin, LoginRequiredMixin,  UpdateView):
    model = Product
    fields = ['name', 'price', 'stock', 'description', 'thumbnail']
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')
    login_url = '/accounts/signin/'
    required_role = 'editor'

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors de l'ajout du produit. Vérifiez les champs et réessayez.")
        return redirect('products')


    def form_valid(self, form):
        old_obj = self.get_object()
        old_data = {
            "name": old_obj.name,
            "price": old_obj.price,
            "stock": old_obj.stock,
            "description": old_obj.description,
        }

        response = super().form_valid(form)
        new_obj = self.object
        new_data = {
            "name": new_obj.name,
            "price": new_obj.price,
            "stock": new_obj.stock,
            "description": new_obj.description,
        }

        # Différences
        changes = clean_json_values({
            key: [old_data[key], new_data[key]]
            for key in old_data if old_data[key] != new_data[key]
        })

        ActivityLog.objects.create(
            activity_id=f"LOG-{new_obj.id}",
            user_email=self.request.user.email,
            user_fullname= self.request.user.fullname,
            ip_address=get_client_ip(self.request),
            action='update',
            object_type='Produit',
            object_id=str(new_obj.id),
            object_name=new_obj.name,
            changes=changes,
            message=f"Produit modifié par {self.request.user.fullname}"
        )

        return response


class ProductDeleteView(RoleRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_content.html'
    success_url = reverse_lazy('products')
    login_url = '/accounts/signin/'
    required_role = 'editor'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        old_data = {
            "name": obj.name,
            "price": obj.price,
            "stock": obj.stock,
            "description": obj.description,
        }
        new_data = {
            "name": obj.name,
            "price": obj.price,
            "stock": obj.stock,
            "description": obj.description,
        }

        # Différences
        changes = clean_json_values({
            key: [old_data[key], new_data[key]]
            for key in old_data if old_data[key] != new_data[key]
        })
        try:
            log = ActivityLog.objects.create(
            activity_id=f"LOG-{obj.id}",
            user_email=self.request.user.email,
            user_fullname= self.request.user.fullname,
            ip_address=get_client_ip(self.request),
            action='delete',
            object_type='Produit',
            object_id=str(obj.id),
            object_name=obj.name,
            changes=changes,
            message=f"Produit supprimé par {self.request.user.fullname}"
        )
            logger.debug(f"Log de suppression créé : {log}")
        except Exception as e:
            print(f"[LOG ERROR] {e}")

        return super().delete(request, *args, **kwargs)



@min_role_required('editor')
def validate_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        product = order.product

        if product and product.stock is not None:
            if product.stock >= order.quantity:
                # Mise à jour du stock
                product.stock -= order.quantity
                product.save()

                # Validation de la commande
                order.statut = 'validated'
                order.save()

                messages.success(request, "Commande validée et stock mis à jour.")
            else:
                messages.error(request, f"Stock insuffisant pour {product.name} (stock actuel : {product.stock}).")
        else:
            messages.error(request, "Produit invalide ou stock non défini.")

    return redirect('index')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def clean_json_values(data):
    def convert(value):
        if isinstance(value, Decimal):
            return float(value)
        return value

    cleaned = {}
    for key, value in data.items():
        if isinstance(value, list) and len(value) == 2:
            old, new = value
            cleaned[key] = [convert(old), convert(new)]
        else:
            cleaned[key] = convert(value)
    return cleaned

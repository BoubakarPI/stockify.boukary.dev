Voici une structure détaillée et étape par étape pour développer ton **Application de Gestion de Stock avec Django** en **3 semaines**.

---

# **🚀 Semaine 1 : Mise en place du backend et gestion CRUD**
## **1️⃣ Initialisation du projet Django**
- Installer Django et créer le projet :
  ```sh
  django-admin startproject stock_manager
  cd stock_manager
  python manage.py startapp inventory
  ```
- Ajouter `inventory` à `INSTALLED_APPS` dans `settings.py`
- Configurer la base de données (SQLite pour commencer)

## **2️⃣ Définition du modèle Produit**
Dans `inventory/models.py` :
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```
- Appliquer la migration :
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```

## **3️⃣ Gestion CRUD avec Django**
Dans `inventory/views.py` :
- Créer les vues basées sur les classes Django :
  ```python
  from django.views.generic import ListView, CreateView, UpdateView, DeleteView
  from django.urls import reverse_lazy
  from .models import Product

  class ProductListView(ListView):
      model = Product
      template_name = "inventory/product_list.html"

  class ProductCreateView(CreateView):
      model = Product
      fields = ['name', 'quantity', 'price']
      template_name = "inventory/product_form.html"
      success_url = reverse_lazy("product_list")

  class ProductUpdateView(UpdateView):
      model = Product
      fields = ['name', 'quantity', 'price']
      template_name = "inventory/product_form.html"
      success_url = reverse_lazy("product_list")

  class ProductDeleteView(DeleteView):
      model = Product
      template_name = "inventory/product_confirm_delete.html"
      success_url = reverse_lazy("product_list")
  ```

- **Configurer les URLS** dans `inventory/urls.py` :
  ```python
  from django.urls import path
  from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

  urlpatterns = [
      path('', ProductListView.as_view(), name='product_list'),
      path('new/', ProductCreateView.as_view(), name='product_create'),
      path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
      path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
  ]
  ```
- **Inclure les URLs** dans `stock_manager/urls.py` :
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('inventory.urls')),
  ]
  ```

---

# **🚀 Semaine 2 : Interface Graphique & Authentification**
## **4️⃣ Améliorer l'interface avec Bootstrap 5**
- Ajouter Bootstrap dans `base.html` :
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  ```
- **Créer un tableau interactif** dans `inventory/templates/inventory/product_list.html` :
  ```html
  {% extends 'base.html' %}
  {% block content %}
  <div class="container mt-4">
      <h2>Gestion des Produits</h2>
      <a href="{% url 'product_create' %}" class="btn btn-primary mb-3">Ajouter un produit</a>
      <table class="table table-striped">
          <thead>
              <tr>
                  <th>Nom</th>
                  <th>Quantité</th>
                  <th>Prix</th>
                  <th>Actions</th>
              </tr>
          </thead>
          <tbody>
              {% for product in object_list %}
              <tr>
                  <td>{{ product.name }}</td>
                  <td>{{ product.quantity }}</td>
                  <td>{{ product.price }}</td>
                  <td>
                      <a href="{% url 'product_update' product.id %}" class="btn btn-warning">Modifier</a>
                      <a href="{% url 'product_delete' product.id %}" class="btn btn-danger">Supprimer</a>
                  </td>
              </tr>
              {% endfor %}
          </tbody>
      </table>
  </div>
  {% endblock %}
  ```

## **5️⃣ Authentification des utilisateurs**
- **Ajouter Django Auth** dans `settings.py` :
  ```python
  LOGIN_REDIRECT_URL = '/'
  LOGOUT_REDIRECT_URL = '/'
  ```
- **Créer un formulaire d'inscription et de connexion** :
  ```sh
  python manage.py startapp accounts
  ```
- **Créer les vues d'authentification** (`accounts/views.py`) :
  ```python
  from django.contrib.auth.forms import UserCreationForm
  from django.urls import reverse_lazy
  from django.views import generic

  class SignUpView(generic.CreateView):
      form_class = UserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'registration/signup.html'
  ```
- **Configurer les URLs d’authentification** (`accounts/urls.py`) :
  ```python
  from django.urls import path
  from .views import SignUpView

  urlpatterns = [
      path('signup/', SignUpView.as_view(), name='signup'),
  ]
  ```
- **Inclure les URLs dans `stock_manager/urls.py`** :
  ```python
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include('accounts.urls')),
  ```
- **Restreindre l’accès** dans `inventory/views.py` :
  ```python
  from django.contrib.auth.mixins import LoginRequiredMixin

  class ProductCreateView(LoginRequiredMixin, CreateView):
      model = Product
      fields = ['name', 'quantity', 'price']
      success_url = reverse_lazy('product_list')
  ```
- **Ajouter un menu utilisateur** dans `base.html` :
  ```html
  <nav>
      {% if user.is_authenticated %}
          <p>Bienvenue, {{ user.username }} | <a href="{% url 'logout' %}">Déconnexion</a></p>
      {% else %}
          <a href="{% url 'login' %}">Connexion</a> | <a href="{% url 'signup' %}">Inscription</a>
      {% endif %}
  </nav>
  ```

---

# **🚀 Semaine 3 : Fonctionnalités Avancées et Finalisation**
## **6️⃣ Fonctionnalités Bonus**
✅ **Recherche** dans `inventory/views.py` :
```python
class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Product.objects.filter(name__icontains=query)
        return super().get_queryset()
```
Dans le template :
```html
<form method="GET">
    <input type="text" name="q" placeholder="Rechercher un produit...">
    <button type="submit">Rechercher</button>
</form>
```

✅ **Export CSV** :
```python
import csv
from django.http import HttpResponse

def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Quantité', 'Prix'])
    for product in Product.objects.all():
        writer.writerow([product.name, product.quantity, product.price])
    return response
```

✅ **Alertes** dans le template :
```html
{% if product.quantity <= 5 %}
    <span class="badge bg-danger">Stock Faible</span>
{% endif %}
```

---

# 🎯 **Livrable final**
- Une application Django fonctionnelle avec une interface responsive
- Authentification sécurisée
- CRUD des produits avec recherche et export CSV
- Présentation propre et interactive

Avec ce plan structuré, ton projet sera bien organisé et réalisable en 3 semaines ! 🚀
from django.contrib import admin
from .models import Product
from .models import Commande
from .models import CommandeItem
# Register your models here.
admin.site.register(Product)
admin.site.register(CommandeItem)
admin.site.register(Commande)

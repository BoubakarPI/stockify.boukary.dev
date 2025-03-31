from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
#class Commande(models.Model):
    
#Pour recuperer la date et le prix total d une commande


class Commande(models.Model):
    STATUT_CHOICES = [
        ('en_entente', 'En entente'),
        ('paye', 'Payé'),
        ('expedie', 'Expédié'),
        ('livre', 'Livré'),
    ]
  #  user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_entente')
    produit=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantite=models.PositiveIntegerField(default=1)

    def total(self):
        total_commande = 0
        for item in self.items.all():
            total_commande += item.sous_total()


class CommandeItem(models.Model):
    commande=models.ForeignKey(Commande,related_name="items",on_delete=models.CASCADE)
    produit=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantite=models.PositiveIntegerField()
    def sous_total(self):
        return self.produit.prix*self.quantite
    


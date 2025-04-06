from django.db import models

from inventory.models import Product


class Order(models.Model):
    STATUT_CHOICES = [
        ('pending', 'En entente'),
        ('paid', 'Payé'),
    ]
    order_date = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='pending')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    phone=models.CharField(max_length=18, null=True)
    address=models.CharField(max_length=128, null=True)
    fullname=models.CharField(max_length=128, null=True)
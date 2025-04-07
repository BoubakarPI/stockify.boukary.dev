import json
from decimal import Decimal

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from accounts.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=125)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})



class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('add', 'Ajout'),
        ('update', 'Modification'),
        ('delete', 'Suppression'),
    ]

    activity_id = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    user_email = models.CharField(max_length=255)
    user_fullname = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    object_type = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    object_name = models.CharField(max_length=255, blank=True)
    changes = models.JSONField(null=True, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_action_display()} - {self.object_type} #{self.object_id}"



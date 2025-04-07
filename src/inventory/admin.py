from django.contrib import admin

from .models import Product, ActivityLog

# Register your models here.
admin.site.register(Product)
admin.site.register(ActivityLog)
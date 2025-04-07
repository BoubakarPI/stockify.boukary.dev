
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import index, logs, export_products_csv, export_orders_csv

urlpatterns = [
    path('', index, name="index"),
    path('logs/', logs, name="logs"),
    path('export/products/', export_products_csv, name='export_products_csv'),
    path('export/orders/', export_orders_csv, name='export_orders_csv'),
    path('store/', include('store.urls')),
    path('products/', include('inventory.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

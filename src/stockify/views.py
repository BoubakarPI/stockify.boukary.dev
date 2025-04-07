import csv
import json

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import User
from store.models import Order
from inventory.models import Product

from inventory.models import ActivityLog


def index(request):
    income = Order.objects.filter(statut='validated').aggregate(
        total_income=Sum(
            ExpressionWrapper(
                F('product__price') * F('quantity'),
                output_field=DecimalField()
            )
        )
    )['total_income']

    # Agrégation par mois, total des ventes validées
    monthly_sales = (
        Order.objects
        .filter(statut='validated')
        .annotate(month=TruncMonth('order_date'))
        .values('month')
        .annotate(total=Sum(F('product__price') * F('quantity')))
        .order_by('month')
    )

    monthly_data = [0] * 12
    for item in monthly_sales:
        month_index = item['month'].month - 1
        monthly_data[month_index] = float(item['total']) if item['total'] else 0


    low_stock_products = Product.objects.filter(stock__lt=6)
    users = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    STATUS_LABELS = {
        'pending': 'En attente',
        'validated': 'Validée',
        'rejected': 'Rejetée',
        'cancelled': 'Annulée',
    }

    order_status_counts = (
        Order.objects.values('statut')
        .annotate(count=Count('id'))
    )

    # Pour envoyer au JS
    labels = [STATUS_LABELS.get(entry['statut'], entry['statut']) for entry in order_status_counts]
    data = [entry['count'] for entry in order_status_counts]


    context = {
        'products': products,
        'users': users,
        'orders': orders,
        'low_stock_products': low_stock_products,
        'income': income,
        'monthly_sales': monthly_data,
        'order_status_labels': json.dumps(labels),
        'order_status_data': json.dumps(data),
    }
    return render(request, 'dashboard.html', context)


def logs(request):
    logs = ActivityLog.objects.all()
    return render(request, 'logs.html', context={'logs': logs,})



@login_required
def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stockify-products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prix', 'Stock', 'Description'])

    for product in Product.objects.all():
        writer.writerow([product.name, product.price, product.stock, product.description])

    return response


@login_required
def export_orders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stockify-orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Client', 'Telephone', 'Adresse', 'Produit', 'Quantite', 'Prix unitaire', 'Montant total', 'Date', 'Statut'])

    for order in Order.objects.select_related('product'):
        total = order.product.price * order.quantity
        writer.writerow([
            order.fullname,
            order.phone,
            order.address,
            order.product.name,
            order.quantity,
            order.product.price,
            total,
            order.order_date,
            order.statut,
        ])

    return response


def unauthorized_view(request):
    return render(request, 'unauthorized.html')

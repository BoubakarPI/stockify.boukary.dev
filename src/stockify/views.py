from django.db.models import Sum, F, ExpressionWrapper, DecimalField
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


    low_stock_products = Product.objects.filter(stock__lt=8)
    users = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    context = {
        'products': products,
        'users': users,
        'orders': orders,
        'low_stock_products': low_stock_products,
        'income': income,
        'monthly_sales': monthly_data,
    }
    return render(request, 'dashboard.html', context)

def logs(request):
    logs = ActivityLog.objects.all()
    return render(request, 'logs.html', context={'logs': logs,})


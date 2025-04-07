
## 🧱 Structure détaillée

```

stockify.boukary.dev/
    ├── requirements.txt
    └── src/
        ├── README.md
        ├── __init__.py
        ├── db.sqlite3
        ├── manage.py
        ├── accounts/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── forms.py
        │   ├── models.py
        │   ├── signals.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── __pycache__/
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   ├── __init__.py
        │   │   └── __pycache__/
        │   └── templates/
        │       └── accounts/
        │           ├── signin.html
        │           ├── signup.html
        │           └── user_content.html
        ├── inventory/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── __pycache__/
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_alter_product_stock.py
        │   │   ├── 0003_activitylog.py
        │   │   ├── __init__.py
        │   │   └── __pycache__/
        │   └── templates/
        │       └── inventory/
        │           ├── product.html
        │           └── product_list.html
        ├── medias/
        │   └── products/
        ├── stockify/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── middleware.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── wsgi.py
        │   ├── __pycache__/
        │   └── templates/
        │       └── index.html
        ├── store/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── forms.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── __pycache__/
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_order_address_order_fullname_order_phone.py
        │   │   ├── 0003_alter_order_statut.py
        │   │   ├── __init__.py
        │   │   └── __pycache__/
        │   └── templates/
        │       └── store/
        │           ├── add_order.html
        │           ├── product_detail.html
        │           └── product_list.html
        └── templates/
            ├── auth_layout.html
            ├── dashboard.html
            ├── layout.html
            ├── logs.html
            ├── product_content.html
            ├── store_layout.html
            └── unauthorized.html

```

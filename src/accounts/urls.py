from .views import signin_view, signup_view
from django.urls import path

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
]
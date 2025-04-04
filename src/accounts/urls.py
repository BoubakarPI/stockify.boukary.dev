from .views import signin_view, signup_view, logout_user
from django.urls import path

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
]
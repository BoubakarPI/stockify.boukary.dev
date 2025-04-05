from .views import signin_view, signup_view, logout_user, AccountListView, CreateUserByAdminView
from django.urls import path

urlpatterns = [
    path('', AccountListView.as_view(), name='accounts'),
    path('add', CreateUserByAdminView.as_view(), name='add'),
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
]
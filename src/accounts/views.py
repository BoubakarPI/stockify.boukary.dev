from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User


# Create your views here.

class AccountListView(ListView):
    model = User
    template_name = 'accounts/user_content.html'

class CreateUserByAdminView(View):
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts')
        return redirect('accounts')


def createAdminUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.role = 'admin'
        user.save()
    return redirect('accounts')

def createEditorUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.role = 'editor'
        user.save()
    return redirect('accounts')


def createViewerUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.role = 'viewer'
        user.save()
    return redirect('accounts')


def deleteUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
    return redirect('accounts')

def signin_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("products")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/signin.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect('index')
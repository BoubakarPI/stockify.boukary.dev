from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
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
            print('+++++++++++++ valid')
            user = form.save()
            return redirect('accounts')
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
    return redirect('home')
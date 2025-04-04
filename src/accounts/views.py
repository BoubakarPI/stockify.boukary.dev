from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
def signin_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/signin.html", {"form": form})


def signup_view(request):
    print(request)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            return redirect("home")  # Redirige vers la page d'accueil
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('home')
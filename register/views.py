from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save() # saves form to database so user can be created
        return redirect("/home")
    
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
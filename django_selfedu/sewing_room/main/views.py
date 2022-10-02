from audioop import reverse
from django.urls import reverse_lazy
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Dress, Categories
from django.views.generic import ListView, CreateView
from .forms import *
from django.contrib.auth.views import LoginView



class Main(ListView):
    model = Dress
    template_name = "main/main.html"


class About(ListView):
    model = Dress
    template_name = "main/about.html"


class Assortment(ListView):
    model = Dress
    template_name = "main/products.html"
    context_object_name = "dresses"


class ShowCategory(ListView):
    model = Dress
    template_name = "main/product_cats.html"
    context_object_name = 'dresses'

    def get_queryset(self):
        return Dress.objects.filter(category_id__slug = self.kwargs['cat_slug'])


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    form = LoginUserForm
    template_name = 'main/login.html'


# def main(request):
#     return render(request, "main/main.html", {"cats": Categories.objects.all()})

# def about(request):
#     return render(request, "main/about.html")

# def show_category(request, cat_slug):
#     dresses = Dress.objects.filter(category_id__slug = cat_slug)
#     return render(request, "main/product_cats.html", {'dresses': dresses})

# def assortment(request):
#     dresses = Dress.objects.all()
#     return render(request, 'main/products.html', {'dresses': dresses})
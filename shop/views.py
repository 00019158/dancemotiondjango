from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Product, Category
from .forms import OrderForm



def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {
        "products": products,
        "categories": categories,
    })



def products_api(request):
    products = Product.objects.all()
    data = []

    for p in products:
        data.append({
            "id": p.id,
            "title": p.title,
            "price": p.price,
            "category": p.category.name,
            "discount": p.discount,
            "is_new": p.is_new,
            "image": p.image.url if p.image else ""
        })

    return JsonResponse(data, safe=False)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  
            order.save()
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(request, "order_form.html", {"form": form})



def order_success(request):
    return render(request, "order_success.html")

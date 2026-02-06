from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(
            request,
            "categories.html",
            {
                "categories": categories
            }
        )

def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(
            request,
            "products.html",
            {
                "products": products
            }
        )

def category_products_view(request, category_id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        return render(
            request,
            "category_products.html",
            {
                "category": category,
                "products": products
            }
        )

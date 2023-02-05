from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product


# Create your views here.
def products(request):
    all_products = Product.objects.all()
    products = [{"id": product.id, "title": product.title} for product in all_products]
    return JsonResponse({"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return JsonResponse(
        {
            "title": product.title,
            "description": product.description,
            "price": str(product.price),
            "inventory_quantity": product.inventory_quantity,
        }
    )

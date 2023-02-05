import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        title = body.get("title")
        description = body.get("description")
        price = body.get("price")
        inventory_quantity = body.get("inventory_quantity")

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            inventory_quantity=inventory_quantity,
        )

        return JsonResponse({"success": True}, status=200)

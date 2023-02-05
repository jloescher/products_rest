import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
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
        },
        status=200,
    )


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        title = body.get("title")
        description = body.get("description")
        price = body.get("price")
        inventory_quantity = body.get("inventory_quantity")
        image_link = body.get("image_link")

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            inventory_quantity=inventory_quantity,
            image_link=image_link,
        )

        return JsonResponse({"product": product.to_dict()}, status=201)


@csrf_exempt
def update_product(request, product_id):
    if request.method == "PUT":
        product = get_object_or_404(Product, pk=product_id)

        body = json.loads(request.body.decode("utf-8"))
        title = body.get("title")
        description = body.get("description")
        price = body.get("price")
        inventory_quantity = body.get("inventory_quantity")
        image_link = body.get("image_link")

        product.title = title
        product.description = description
        product.price = price
        product.inventory_quantity = inventory_quantity
        product.image_link = image_link
        product.save()

        return JsonResponse({"product": product.to_dict()}, status=200)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return HttpResponse(status=204)

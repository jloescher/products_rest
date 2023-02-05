from django.urls import path
from .views import products, product_detail, create_product, update_product

urlpatterns = [
    path("products/", products, name="products"),
    path("products/<int:product_id>/", product_detail, name="product_detail"),
    path("products/create/", create_product, name="create_product"),
    path("products/<int:product_id>/update/", update_product, name="update_product"),
]

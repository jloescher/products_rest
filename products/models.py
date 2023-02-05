from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(
        max_length=255
    )  # Pretty sure IRL this would be a TextField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image_link = models.CharField(
        max_length=255, default="https://via.placeholder.com/300"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": str(self.price),
            "inventory_quantity": self.inventory_quantity,
            "image_link": self.image_link,
        }

    def update_product(product, request_body):
        for field in request_body:
            if hasattr(product, field) and request_body[field] is not None:
                setattr(product, field, request_body[field])
        product.save()
        return product

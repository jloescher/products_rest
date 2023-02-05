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

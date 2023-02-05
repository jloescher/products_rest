from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(
        max_length=255
    )  # Pretty sure IRL this would be a TextField
    price = models.DecimalField()
    inventory_quantity = models.IntegerField()

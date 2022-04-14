from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)

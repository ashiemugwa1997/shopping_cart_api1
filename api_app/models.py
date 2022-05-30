from django.db import models
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=180)
    product_price = models.FloatField(max_length=180)
    product_quantity = models.IntegerField()
    updated = models.DateTimeField(auto_now=True, blank=True)

    def _str_(self):
        return self.product_name

# Create your models here.

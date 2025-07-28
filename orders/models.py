from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True, primary_key=True)
    customer_name = models.CharField(max_length=200)
    freight = models.DecimalField(max_digits=10, decimal_places=2)
    ship_name = models.CharField(max_length=200)
    ship_country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"

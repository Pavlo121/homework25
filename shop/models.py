from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(1)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

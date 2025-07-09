from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_address=models.TextField()
    total_price=models.DecimalField(decimal_places=2,max_digits=10)
    created_at=models.DateTimeField(auto_now_add=True)
    status_choices=[
        ('pending','pending'),
        ('processing','processing'),
        ('shipped','shipped'),
        ('delivered','delivered')
    ]
    status=models.CharField(max_length=20,choices=status_choices,default='pending')

    def __str__(self):
        return f"order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

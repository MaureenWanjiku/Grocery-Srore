from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    details = models.TextField(default='')

class offer(models.Model): 
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    def add_product(self, product):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()

    def total_items(self):
        return self.cartitem_set.aggregate(models.Sum('quantity'))['quantity__sum'] or 0

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
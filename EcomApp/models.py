from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

# Create your models here.
#custom manager 
class CustomManager(models.Manager):
    def get_price_range(self,r1,r2):
        return self.filter(price__range=(r1,r2))
    
    def watch_list(self):
        return self.filter(category__exact="Watch")
    
    def price_sort(self) -> QuerySet:
        return super().get_queryset().order_by('-price')

class Product(models.Model):
    product_id =models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=55)
    type=(('Mobile','Mobile'),('Watch','Watch'),('Laptops','Laptops'))
    category=models.CharField(max_length=50, choices=type)
    desc=models.CharField(max_length=300)
    price=models.IntegerField()
    image=models.ImageField(upload_to="pics")
    user = models.ForeignKey(User,on_delete =models.CASCADE, default = 1)

    prod = CustomManager()
    objects=models.Manager() #default

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete =models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete =models.CASCADE, default = 1)

class Order(models.Model):
    order_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete =models.CASCADE, default = 1)
    is_completed = models.BooleanField(default= False)
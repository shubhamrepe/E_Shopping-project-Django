from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Product,CartItem,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=["product_id","product_name","price","image"]

admin.site.register(Product,ProductAdmin)


class Cartadmin(admin.ModelAdmin):
    list_display=["product","quantity","user"]


admin.site.register(CartItem,Cartadmin)

class Orderadmin(admin.ModelAdmin):
     list_display= ["order_id","product_id","quantity","user","is_completed"]

admin.site.register(Order,Orderadmin)
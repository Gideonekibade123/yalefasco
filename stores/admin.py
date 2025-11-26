from django.contrib import admin

# Register your models here.
from . models import Cart
from . models import CartProduct
from . models import Collection
from . models import Category
from . models import Product
from . models import Order

admin.site.register(Category)
admin.site.register(Collection) 
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)  

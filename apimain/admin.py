from django.contrib import admin
from . models import IngredientQuantity, Inventory, Products, Orders


# Register your models here.
admin.site.register(Inventory)
admin.site.register(Products)
admin.site.register(IngredientQuantity)
admin.site.register(Orders)
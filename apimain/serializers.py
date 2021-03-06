from django.contrib.auth import models
from rest_framework import fields, serializers
from rest_framework.compat import md_filter_add_syntax_highlight
from . models import Inventory, IngredientQuantity, Products, Orders
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

#Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['ingredient']

#Ingredient Quantity Serialzer
class IngredientQuantitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = ['inventory', 'product', 'quantity']

#Products Serializer
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product', 'cost_price', 'selling_price', 'all_ingridient']

# All Products Serializer
class AvialableProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product']

#Oders Serializer
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['user', 'product']





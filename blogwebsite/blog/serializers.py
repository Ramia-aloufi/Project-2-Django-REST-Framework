from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Article
from .models import Products
from .models import Customers
from .models import Orders
from .models import Reviews


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price']


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'firstName', 'lastName']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'title', 'customer', 'product', 'quantity', 'created_At']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'title', 'customer', 'product', 'rating', 'review']


# def validate(self, attrs):
#     unknown = set(self.initial_data) - set(self.fields)
#     if unknown:
#         raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
#     return attrs

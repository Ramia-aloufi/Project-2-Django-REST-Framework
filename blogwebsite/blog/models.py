from django.db import models

# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=1)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=1)
    review = models.IntegerField(max_length=1)


    def __str__(self):
        return self.title

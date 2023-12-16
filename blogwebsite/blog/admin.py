from django.contrib import admin
from .models import Article
from .models import Products
from .models import Customers
from .models import Orders
from .models import Reviews

# Register your models here.
admin.site.register(Article)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Reviews)



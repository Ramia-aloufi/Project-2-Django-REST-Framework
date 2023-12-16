from .models import Article
from .models import Products
from .models import Customers
from .models import Orders
from .models import Reviews
from .serializers import ArticleSerializer
from .serializers import CustomersSerializer
from .serializers import ProductsSerializer
from .serializers import OrdersSerializer
from .serializers import ReviewsSerializer




from rest_framework import mixins
from rest_framework import viewsets


class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


class CustomerViewSet(viewsets.GenericViewSet,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()


class RiveViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()


class OrderViewSet(viewsets.GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

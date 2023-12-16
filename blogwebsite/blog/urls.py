from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('product', ProductViewSet, basename='product')
router.register('customer', CustomerViewSet, basename='customer')
router.register('review', RiveViewSet, basename='review')
router.register('order', OrderViewSet, basename='order')



urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),


]

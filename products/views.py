from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from .permissions import IsShopOwner 

class ProductListView(generics.ListCreateAPIView):
    """
    List all active products(public) or create product(shop owner)
    """

    queryset =Product.objects.filter(is_active=True)

    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filter_fields = ['category_slug', 'price', 'is_active']

    search_fields = ['name', 'description']

    ordering_fields = ['price', 'created_at', 'stock']

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve , update, delete a product by slug
    """
    queryset = Product.objects.all()

    serializer_class =ProductSerializer

    permission_classes = [IsAdminOrReadOnly]

    lookup_field = 'slug'

class CategoryListView(generics.ListAPIView):
    """
    List all categories
    """
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

class InventorySummaryView(generics.GenericAPIView):
   """
   For shop owner: total inventory value
   """
   permisson_classes = [IsShopOwner]

   def get(self,request):
       total_value = sum(product.total_value for product in Product.objects.all())
       return Response({'total_inventory_value_kes': total_value})
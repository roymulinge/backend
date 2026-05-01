from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
    
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all(), write_only=True
    )
    total_value =serializers.DecimalField(
        source='total_value', read_only=True, max_digits=12, decimal_places=2
    )
    
    class Meta:
        model =Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'stock',
            'category', 'category_id', 'image', 'is_active',
            'created_at', 'updated_at', 'total_value'
        ]
        read_only_fields = ['created_at', 'updated_at', 'total_value']

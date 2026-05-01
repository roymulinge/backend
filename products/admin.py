from django.contrib import admin
from .models import Category, Product

@admin.register(Category)

class CategoryAdmin(admin.modelAdmin):
    prepopulated_fileds = {'slug', ('name', )}
    lis_display = ('name', 'created_at')

@admin.register(Product)

class ProductAdmin(admin.modelAdmin):
    prepopulated_fileds = {'slug', ('name',)}
    list_display = ('name', 'price', 'stock', 'category', 'is_active', 'total_value')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('total_value')
    
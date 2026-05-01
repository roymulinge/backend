from django.db import models

class Catergory(models.Model):
     name = models.CharField(max_length=100, unique=True)
     slug = models.CharField(unique=True)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          verbose_name_plural = 'Categories'

     def __str__(self):
          return self.name
     
class Product(models.Model):
     name = models.CharField(max_length=255)
     slug = models.SlugField(unique=True)
     description = models.TextField()
     price = models.DecimalField(max_length=100, decimal_places=2) #KES
     stock = models.PositiveIntegerField()
     category = models.ForeignKey(Catergory, on_delete=models.SET_NULL, null=True, blank=True)
     image = models.ImageField(upload_to='products/', blank=True, null=True)
     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.name
     
     @property
     def total_value(self):
          """
          Total value of stock for this product(price * stock)
          """
          return self.price * self.stock



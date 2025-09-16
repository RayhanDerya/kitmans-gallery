import uuid
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('menswear', 'Menswear'),
        ('womenswear', 'Womenswear'),
        ('kidswear', 'Kidswear'),
        ('exclusive', 'Exclusive'),
        ('accessories', 'Accessories'),
    ]
    
    
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
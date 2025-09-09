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
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
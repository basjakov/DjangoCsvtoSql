from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRODUCT_CHOICES = (
    ('Ershik','ershik'),
    ('Paxpaxak','paxpaxak'),
    ('Pnduk','pnduk'),
    ('Chocolate','chocolate'),
)
class product(models.Model):
    product = models.CharField(max_length=11,choices=PRODUCT_CHOICES)
    productowner = models.CharField(max_length=13)
    count = models.CharField(max_length=13)
    price = models.CharField(max_length=13)
    updated = models.DateField(auto_now=True)
    created= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.count}"
            
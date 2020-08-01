from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRODUCT_CHOICES = (
    ('TV','tv'),
    ('IPAD','ipad'),
    ('PLAYSTATION','playstation'),
)
class product(models.Model):
    product = models.CharField(max_length=11,choices=PRODUCT_CHOICES)
    productowner = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    updated = models.DateField(auto_now=True)
    created= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.count}"
    def save(self,*args,**kwargs):
        price = None
        if self.product == 'TV':
           price = 168
        elif self.product == 'IPAD':
            price == 400
        else:
            pass
        self.total = price * self.count
        super().save(*args,**kwargs)           
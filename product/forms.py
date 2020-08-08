from django import forms
from .models import product
from django.forms import ModelForm

class myproductForm(ModelForm):
    class Meta:
        model = product
        fields = ('product','productowner','count','price')
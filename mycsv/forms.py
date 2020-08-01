from django import forms
from .models import mycsv
from django.forms import ModelForm

class mycsvForm(ModelForm):
    class Meta:
        model = mycsv
        fields = ('file_name',)
from django.urls import path
from .views import upload_field

app_name="Webster_CSV"

urlpatterns = [
    path('confirm/',upload_field,name="upload_field"),

]
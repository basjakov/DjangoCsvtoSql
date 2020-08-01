#from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import mycsvForm
from .models import mycsv
from product.models import product
import csv
# Create your views here.
def upload_file_view(request):
 
    form = mycsvForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form = mycsvForm()
        obj = mycsv.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader = csv.reader(f)

            for i,row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row = "".join(row)
                    row = row.split(";")
                    product = row[1]
                    print(row)
                    product.objects.create(
                         product = product,
                         count = int(row[2]),
                         productowner = row[3],
                     )
            obj.activated == True
            obj.save()
    return render(request,'mycsv/upload.html',{'form':form})
#from django.shortcuts import render
from django.shortcuts import render

from .forms import mycsvForm
from .models import mycsv
import csv
from product.models import product
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
                    print(row)
                    product.objects.create(
                           product = row[1],
                           productowner = row[3],
                           count = int(row[2]),
                           price = int(row[4]),
                     )
            obj.activated == True
            obj.save()
    return render(request,'mycsv/upload.html',{'form':form})
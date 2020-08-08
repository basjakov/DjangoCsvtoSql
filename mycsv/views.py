#from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect

from .forms import mycsvForm
from .models import mycsv


import csv

# Create your views here.
def upload_file_view(request):
    fields  = ()
    form = mycsvForm(request.POST or None,request.FILES or None)
  
    if form.is_valid():
        
        form.save()
        
        obj = mycsv.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader = csv.reader(f)

            for i,row in enumerate(reader):
                    row = "".join(row)
                    row = row.split(";")
                    fields += tuple(row)
            
            obj.save()
            return render(request,'mycsv/fieldsdump.html',{'fields':fields}) 
    return render(request,'mycsv/upload.html',{'form':form,'fields':fields})   

      
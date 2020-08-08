from django.shortcuts import render,HttpResponseRedirect
from django.forms import ModelForm
from .forms import myproductForm
from mycsv.models import mycsv
from .models import product


import csv
# Create your views here.

def upload_field(request):
    if request.method == 'POST':
           
            form = myproductForm(request.POST)    
            product = request.POST.get('product')
            productowner = request.POST.get('productowner')
            count = request.POST.get('count')
            price = request.POST.get('price')
            obj = mycsv.objects.get(activated=False)    
            
            if form.is_valid():   
                form.save() 
                form = myproductForm() 
                
            with open(obj.file_name.path,'r') as f:
                        reader = csv.reader(f)        
                        for i,row in enumerate(reader):
                            if i==0:
                                pass
                            else: 
                                row = "".join(row)
                                row = row.split(";")                           
                                if product == "productowner":
                                        product = row[3]        
                                if product == "product":
                                        product = row[1] 
                                if product == "count" or "price":
                                    print("this table don't  have integer types")   
                                if productowner == "product":
                                        productowner = row[1]
                                if productowner == "productowner":
                                        productowner = row[3]
                                if productowner == "count" or "price":
                                    print("this table don't  have integer types")              
                                if count == "price":
                                        count = int(row[4])
                                if count == "count":
                                        count = int(row[2])
                                if count == "productowner" or "product":       
                                    print("this table don't  have integer types")
                                if price == "count":
                                        price = int(row[2])
                                if price == "price":
                                        count = int(row[4])
                                if price == "productowner" or "product":       
                                    print("this table don't  have integer types")
                                product.objects.create(
                                        product = product,
                                        productowner = productowner,
                                        count = str(count),
                                        price = str(price),
                                )
            obj.save()
            return HttpResponseRedirect('/')
      
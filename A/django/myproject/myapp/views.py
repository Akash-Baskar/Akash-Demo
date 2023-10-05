# from cgitb import text
# from importlib.resources import contents
# import pandas as pd


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import TemplateView

# # Create your views here.
# def index(request):
#     return render(request,'index.html')


# def file(request):
    
    
#     return render(request,'file.html',{'amount':contents})
   


    

import csv
from django.shortcuts import render
from django.http import JsonResponse

 

def index(request):
    return render(request, 'index.html')

 

def upload_and_display_csv(request):
    if request.method == 'POST' and request.FILES.get('csvFile'):
        csv_file = request.FILES['csvFile']
        csv_data = csv_file.read().decode('utf-8')

 

        # Parse CSV data
        csv_reader = csv.reader(csv_data.splitlines())
        header = next(csv_reader)  # Header row
        data_rows = list(csv_reader)

 

        return render(request, 'file.html', {'header': header, 'data_rows': data_rows})
    else:
        return render(request, 'index.html')



 




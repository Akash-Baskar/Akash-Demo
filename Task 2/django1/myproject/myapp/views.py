from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


    
def age(request):
    file=open('C:/Users/AkashBaskar/Desktop/Task 01/django1/myproject/myapp/t1.txt',"r")
    contents=file.read()
    file.close()
    return render(request,'age.html',{'amounts':contents})


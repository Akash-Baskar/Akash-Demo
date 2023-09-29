from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


    


def age(request):
    text=request.GET['text']
    file=open("C:/Users/AkashBaskar/Desktop/Task 2/django1/myproject/myapp/t1.txt","a")
    words=file.write(f"{text} \n")
    file.close()
    return render(request,'age.html',{'amounts':words})
    


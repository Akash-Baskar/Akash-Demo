from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def age(request):
    birth_year=request.GET['text']
    li = birth_year.split("-")
    return render(request,'age.html',{'amounts':2023-int(li[0])})
    
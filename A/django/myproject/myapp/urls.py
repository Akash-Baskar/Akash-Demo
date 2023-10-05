# from operator import index
# from django.contrib import admin
# from django.urls import path
# from .import views
# urlpatterns=[
#     path('', views.index,name='index'),
#     path('file',views.file,name='file')
    
# ]

from django.urls import path
from . import views

 

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_csv/', views.upload_and_display_csv, name='upload_and_display_csv'),
]
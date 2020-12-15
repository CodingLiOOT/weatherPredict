from django.shortcuts import render
from web_ui.settings import STATIC_URL
from . import views
from django.conf.urls import  url
# Create your views here.
def weather(request):
    return render(request,"index.html")
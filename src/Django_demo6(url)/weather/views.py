from django.shortcuts import render,redirect,HttpResponseRedirect
from django.shortcuts import HttpResponse
from web_ui.settings import STATIC_URL
from . import views
from weather.models import User
from weather import models
from django.conf.urls import url
import json
import weather



# Create your views here.
def register(request):
    if request.method == "GET":
        name = request.GET.get('name')
        password = request.GET.get('pw')
        ID = len(User.objects.all())+18301000
        User.objects.create(userID=str(ID),userName=name,userPassword=password)
        return HttpResponse(str(ID))

def checkLogin(request):
    if request.method == "GET":
        id = request.GET.get('id')
        password = request.GET.get('pw')
        try:
            if password == User.objects.get(userID=id).userPassword:

                #return HttpResponseRedirect("http://127.0.0.1:8000/weather")

                #return HttpResponseRedirect("https://www.baidu.com")
                return HttpResponse("true")
                #Weather(request)
            else:

                return HttpResponse("false")
        except weather.models.User.DoesNotExist:

            return HttpResponse("false")


def registerWeb(request):
    return render(request, 'register.html')


def loginWeb(request):
    return render(request, 'login.html')


def Weather(request):
    string = '''
    {
        "weather" : [
        {
            "Date": "2020/7/4",
            "tmax": "88.69067914",
            "tmin": "72.82230891"
        }
        ,
        {
            "Date": "2020/7/5",
            "tmax": "89.86402112",
            "tmin": "75.2151643"
        }
        ,
        {
            "Date": "2020/7/6",
            "tmax": "88.49302504",
            "tmin": "71.50879918"
        }
        ,
        {
            "Date": "2020/7/7",
            "tmax": "90.21692641",
            "tmin": "72.69614125"
        }
        ,
        {
            "Date": "2020/7/8",
            "tmax": "86.37840625",
            "tmin": "71.83584324"
        }
        ,
        {
            "Date": "2020/7/9",
            "tmax": "88.17650449",
            "tmin": "70.97347528"
        }
        ,
        {
            "Date": "2020/7/10",
            "tmax": "77.07934732",
            "tmin": "72.04385392"
        }
        ,
        {
            "Date": "2020/7/11",
            "tmax": "86.87683151",
            "tmin": "70.51389907"
        }
        ,
        {
            "Date": "2020/7/12",
            "tmax": "87.96489974",
            "tmin": "72.72124037"
        }
        ,
        {
            "Date": "2020/7/13",
            "tmax": "91.93134482",
            "tmin": "71.94020588"
        }
        ,
        {
            "Date": "2020/7/14",
            "tmax": "88.49797387",
            "tmin": "72.26336489"
        }
        ,
        {
            "Date": "2020/7/15",
            "tmax": "89.53476323",
            "tmin": "71.98730797"
        }
        ,
        {
            "Date": "2020/7/16",
            "tmax": "90.38905863",
            "tmin": "72.12773706"
        }
        ,
        {
            "Date": "2020/7/17",
            "tmax": "88.51943837",
            "tmin": "72.3333465"
        }
        ,
        {
            "Date": "2020/7/18",
            "tmax": "86.87373352",
            "tmin": "72.24034331"
        }
        ,
        {
            "Date": "2020/7/19",
            "tmax": "86.54009703",
            "tmin": "72.60874857"
        }
    ]
    }
    '''



    weather = [{'str': string}]
    return render(request, "index.html", {
        'Weather': json.dumps(weather)
    })


def cityWeather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        # print(city)
        if city == 'shanghai':
            str = '''
                {
"weather": [
{
    "Date": "2020/7/4",
    "tmax": "88",
    "tmin": "72"
}
,
{
    "Date": "2020/7/5",
    "tmax": "100",
    "tmin": "100"
}
,
{
    "Date": "2020/7/6",
    "tmax": "88",
    "tmin": "71"
}
,
{
    "Date": "2020/7/7",
    "tmax": "100",
    "tmin": "100"
}
,
{
    "Date": "2020/7/8",
    "tmax": "100",
    "tmin": "100"
}
,
{
    "Date": "2020/7/9",
    "tmax": "88",
    "tmin": "70"
}
,
{
    "Date": "2020/7/10",
    "tmax": "77",
    "tmin": "72"
}
,
{
    "Date": "2020/7/11",
    "tmax": "86",
    "tmin": "70"
}
,
{
    "Date": "2020/7/12",
    "tmax": "87",
    "tmin": "72"
}
,
{
    "Date": "2020/7/13",
    "tmax": "100",
    "tmin": "100"
}
,
{
    "Date": "2020/7/14",
    "tmax": "88",
    "tmin": "72"
}
,
{
    "Date": "2020/7/15",
    "tmax": "89",
    "tmin": "71"
}
,
{
    "Date": "2020/7/16",
    "tmax": "90",
    "tmin": "72"
}
,
{
    "Date": "2020/7/17",
    "tmax": "88",
    "tmin": "72"
}
,
{
    "Date": "2020/7/18",
    "tmax": "86",
    "tmin": "72"
}
,
{
    "Date": "2020/7/19",
    "tmax": "86",
    "tmin": "72"
}
]
}
           '''
            return HttpResponse(str)
        else:
            str = '''
                            {
            "weather": [
            {
                "Date": "2020/7/4",
                "tmax": "120",
                "tmin": "120"
            }
            ,
            {
                "Date": "2020/7/5",
                "tmax": "100",
                "tmin": "100"
            }
            ,
            {
                "Date": "2020/7/6",
                "tmax": "120",
                "tmin": "120"
            }
            ,
            {
                "Date": "2020/7/7",
                "tmax": "120",
                "tmin": "120"
            }
            ,
            {
                "Date": "2020/7/8",
                "tmax": "120",
                "tmin": "100"
            }
            ,
            {
                "Date": "2020/7/9",
                "tmax": "88",
                "tmin": "70"
            }
            ,
            {
                "Date": "2020/7/10",
                "tmax": "77",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/11",
                "tmax": "86",
                "tmin": "70"
            }
            ,
            {
                "Date": "2020/7/12",
                "tmax": "87",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/13",
                "tmax": "100",
                "tmin": "100"
            }
            ,
            {
                "Date": "2020/7/14",
                "tmax": "88",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/15",
                "tmax": "89",
                "tmin": "71"
            }
            ,
            {
                "Date": "2020/7/16",
                "tmax": "90",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/17",
                "tmax": "88",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/18",
                "tmax": "86",
                "tmin": "72"
            }
            ,
            {
                "Date": "2020/7/19",
                "tmax": "86",
                "tmin": "72"
            }
            ]
            }
                       '''
            return HttpResponse(str)

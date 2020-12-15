from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import HttpResponse
from web_ui.settings import STATIC_URL
# from . import views
from weather.models import User
from weather import models
from django.conf.urls import url
import json
import weather
import websockets
import asyncio


# Create your views here.


def register(request):
    if request.method == "GET":
        name = request.GET.get('name')
        password = request.GET.get('pw')
        ID = len(User.objects.all()) + 18301000
        User.objects.create(userID=str(ID), userName=name, userPassword=password)
        return HttpResponse(str(ID))


def checkLogin(request):
    if request.method == "GET":
        id = request.GET.get('id')
        password = request.GET.get('pw')

        try:
            if password == User.objects.get(userID=id).userPassword:

                return HttpResponse("true")

            else:

                return HttpResponse("false")
        except weather.models.User.DoesNotExist:

            return HttpResponse("false")


def registerWeb(request):
    return render(request, 'register.html')


def loginWeb(request):
    return render(request, 'login.html')


def Weather(request):
    # 写入发送信息，websocket文件读取到消息改变后，发送信息，flask端返回一个字符串写入data.txt文件
    file = open("E:/PythonProject/web/resource/city.txt", mode='w')
    file.write('beijing')
    file.close()
    # 读取data.txt文件，当城市ID与请求ID相同，返回值，否则循环读文件
    file = open('E:/PythonProject/web/resource/data.txt', mode='r')
    strs = file.readlines()
    str = ""
    for text in strs:
        str += text
    weather = [{'str': str}]
    file.close()
    jsObject = json.loads(str)

    while jsObject['data'][1]['Id'] != 'beijing':
        file = open('E:/PythonProject/web/resource/data.txt',mode='r')
        strs = file.readlines()
        str = ""
        for text in strs:
            str += text
        if str=="":
            continue
        weather = [{'str': str}]
        file.close()
        jsObject = json.loads(str)

    return render(request, "index.html", {
        'Weather': json.dumps(weather)
    })


def cityWeather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        file = open("E:/PythonProject/web/resource/city.txt", mode='w')
        ##file.seek(0)
        file.write(city)
        file.close()
        # 读取data.txt文件，当城市ID与请求ID相同，返回值，否则循环读文件
        file = open('E:/PythonProject/web/resource/data.txt', mode='r')
        # file.seek(0)
        strs = file.readlines()
        str = ""
        for text in strs:
            str += text
        file.close()
        # print(str)
        jsObject = json.loads(str, strict=False)

        while jsObject['data'][1]['Id'] != city:
            file = open('E:/PythonProject/web/resource/data.txt', mode='r')
            # file.seek(0)
            strs = file.readlines()
            str = ""
            for text in strs:
                str += text
            file.close()
            if str == "":
                continue
            jsObject = json.loads(str, strict=False)
            # print(jsObject['data'][1]['Id'])
        return HttpResponse(str)

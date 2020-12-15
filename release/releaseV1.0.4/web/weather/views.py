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
from web_ui.settings import BASE_DIR

# Create your views here.

isLogin = False

def logout(request):
    if request.method == "GET":
        global isLogin
        isLogin=False
        return HttpResponse("true")

def register(request):
    if request.method == "GET":
        name = request.GET.get('name')
        password = request.GET.get('pw')
        ID = len(User.objects.all()) + 18301000
        User.objects.create(userID=str(ID), name=name, password=password,userPermission=False)
        return HttpResponse(str(ID))


def checkLogin(request):


    if request.method == "GET":
        id = request.GET.get('id')
        password = request.GET.get('pw')

        try:
            logUser = User.objects.get(userID=id)
            if password == logUser.password:

                global isLogin
                isLogin = True
                if logUser.userPermission:
                    return HttpResponse("manager")
                else:
                    return HttpResponse("normal")

            else:

                return HttpResponse("false")
        except weather.models.User.DoesNotExist:

            return HttpResponse("false")


def registerWeb(request):
    return render(request, 'register.html')


def loginWeb(request):
    return render(request, 'login.html')

def low_weather(request):
    global isLogin
    if isLogin == False:
        return render(request, 'protect.html')
    # 写入发送信息，websocket文件读取到消息改变后，发送信息，flask端返回一个字符串写入data.txt文件
    # file = open("E:/PythonProject/web/resource/city.txt", mode='w')
    file = open(BASE_DIR + "/weather/resource/city.CFG", mode='w')
    file.write('beijing')
    file.close()

    while True:
        # file = open('E:/PythonProject/web/resource/data.txt',mode='r')
        file = open(BASE_DIR + "/weather/resource/data.json", mode='r')
        strs = file.readlines()
        str = ""
        file.close()
        for text in strs:
            str += text
        if str == "":
            continue
        weather = [{'str': str}]

        jsObject = json.loads(str, strict=False)
        if jsObject['data'][1]['Id'] == 'beijing':
            break
    return render(request, "lower_index.html", {
        'Weather': json.dumps(weather)
    })
def Weather(request):
    global isLogin
    if isLogin == False:
        return render(request,'protect.html')
    # 写入发送信息，websocket文件读取到消息改变后，发送信息，flask端返回一个字符串写入data.txt文件
    #file = open("E:/PythonProject/web/resource/city.txt", mode='w')
    file = open(BASE_DIR+"/weather/resource/city.CFG",mode='w')
    file.write('beijing')
    file.close()


    while True:
        #file = open('E:/PythonProject/web/resource/data.txt',mode='r')
        file = open(BASE_DIR+"/weather/resource/data.json",mode='r')
        strs = file.readlines()
        str = ""
        file.close()
        for text in strs:
            str += text
        if str=="":
            continue
        weather = [{'str': str}]

        jsObject = json.loads(str,strict=False)
        if jsObject['data'][1]['Id']=='beijing':
            break
    return render(request, "index.html", {
        'Weather': json.dumps(weather)
    })


def cityWeather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        #file = open("E:/PythonProject/web/resource/city.txt", mode='w')
        ##file.seek(0)
        file = open(BASE_DIR+"/weather/resource/city.CFG",mode='w')
        file.write(city)
        file.close()
        # 读取data.txt文件，当城市ID与请求ID相同，返回值，否则循环读文件



        while True:
            #file = open('E:/PythonProject/web/resource/data.txt', mode='r')
            # file.seek(0)
            file = open(BASE_DIR+"/weather/resource/data.json",mode='r')
            strs = file.readlines()
            str = ""
            for text in strs:
                str += text
            file.close()
            if str == "":
                continue
            jsObject = json.loads(str, strict=False)
            print(jsObject['data'][1]['Id'])
            if(jsObject['data'][1]['Id']==city):
                break
        return HttpResponse(str)

"""web_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather.views import Weather
from weather.views import cityWeather
from django.conf import settings
from weather.views import loginWeb
from weather.views import registerWeb
from weather.views import checkLogin
from django.conf.urls.static import static
from weather.views import register

urlpatterns = [
                  path('weather/', Weather),
                  path('city/', cityWeather),
                  path('login/',loginWeb),
                  path('login/register.html/',registerWeb),
                  path('admin/', admin.site.urls),
                  path('login/check/',checkLogin),
                  path('login/register.html/register/',register),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

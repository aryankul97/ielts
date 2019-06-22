"""IELTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', register),
    path('home/register/login/check/checkscorepage/', checkscorepage),
    path('home/register/login/check/checkscore/', checkscore),
    path('home/contact-us/', contactpage),
    path('home/rules/', rulespage),
    path('home/analytics/', analyticspage),
    path('home/register/', register),
    path('home/register/login/', login),
    path('home/register/login/check/', checklogin),
    path('home/register/login/check/start/', start),
    path('home/register/saveuser/', saveuser),
    path('home/register/saveuser/acceptpolicy/', acceptpolicy),
]

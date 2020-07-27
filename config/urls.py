"""config URL Configuration

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
from theapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('404/', views.error, name='error'),
    path('blank/', views.blank, name='blank'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('forgot-password/', views.password, name='password'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
    path('utilities-animation/', views.animation, name='animation'),
    path('utilities-border/', views.border, name='border'),
    path('utilities-color/', views.color, name='color'),
    path('utilities-other/', views.other, name='other'),
    path('participating-vote/', views.participate, name='participate'),
]
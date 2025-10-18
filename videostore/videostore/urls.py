"""
URL configuration for videostore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from movies import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('create/', views.video_create, name='video_create'),
    path('update/<int:pk>/', views.video_update, name='video_update'),
    path('delete/<int:pk>/', views.video_delete, name='video_delete'),
]

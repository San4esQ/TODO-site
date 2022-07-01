from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.preview),
    path('register/', views.register),
    path('entry/', views.entry),
    path('index/', views.index),
    path('add/', views.add),
    path('index/<int:num>', views.detail),
    path('index/edit/<int:num>', views.edit),
    path('index/delete/<int:num>', views.delete),
    path('test/', views.test),
]

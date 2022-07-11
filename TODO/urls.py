from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', views.register),
    path('', views.entry),
    path('auth/logout/', views.logout),
    path('index/', views.index),
    path('add/', views.add),
    path('index/<int:num>', views.detail),
    path('index/edit/<int:num>', views.edit),
    path('index/delete/<int:num>', views.delete),
]

from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', views.register),
    path('', views.index),
    path('auth/login/', views.entry),
    path('auth/logout/', views.logout),
    path('add/', views.add),
    path('<int:num>', views.detail),
    path('edit/<int:num>', views.edit),
    path('delete/<int:num>', views.delete),
]

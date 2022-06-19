from django.urls import path
from firstapp import views

urlpatterns = [

    path('index/', views.index),
    path('add/', views.add),
    path('index/<int:num>', views.detail),
    path('index/edit/<int:num>', views.edit),
    path('index/delete/<int:num>', views.delete),
]

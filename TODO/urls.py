from django.urls import path
from firstapp import views

urlpatterns = [

    path('index/', views.index),
    path('add/', views.add),
    path('index/<int:num>', views.view),
    path('index/edit/<int:num>', views.edit)
]

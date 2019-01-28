from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.powerball,name='powerball'),
    path('powerball/',views.powerball,name='powerball'),
]
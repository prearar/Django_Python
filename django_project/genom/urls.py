from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='genom-home'),
    path('judge/',views.judge, name='genom-judge')
]

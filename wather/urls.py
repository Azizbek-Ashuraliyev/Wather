from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  #the path for our index view
]
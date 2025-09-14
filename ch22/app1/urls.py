
from django.contrib import admin
from django.urls import path
from app1.views import all_data

urlpatterns = [
    path("all/", all_data, name='all_data'),
]
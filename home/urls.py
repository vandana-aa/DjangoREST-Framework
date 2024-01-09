from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),  # Add a comma here
    path('student/', post_student),
]
from django.urls import path
from .views import * 

# Create your views here.

urlpatterns = [
    path('studentapi/', student_api, name='studentapi'),
]
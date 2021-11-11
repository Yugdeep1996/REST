from django.urls import path
from .views import * 

# Create your views here.

urlpatterns = [
    path('studentapi/', StudentAPI.as_view()),
    path('studentapi/<int:pk>', StudentAPI.as_view()),
]
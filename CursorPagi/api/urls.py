from django.urls import path
from .views import *

urlpatterns = [
    path('studentapi/', StudentList.as_view()),
]
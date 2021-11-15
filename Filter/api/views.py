from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

# http://127.0.0.1:8000/api/studentapi/?city=faridabad&name=yugdeep for results
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # for all views view settings file 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # overriding queryset
#     def get_queryset(self):
#         user = self.request.user
#         # print('user', user)
#         return Student.objects.filter(passby=user)
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:pk>', student_detail, name="student_detail"),
    path('detail/', student_list, name="student_list"),
    path('deser_stu/', des_student, name="deser_stu"),
    path('crud_stu/', Crud_student.as_view(), name="crud_stu"),
    # path('get_up_stu/', up_student, name="get_up_stu"),
]
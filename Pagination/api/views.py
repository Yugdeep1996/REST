from rest_framework.generics import ListAPIView

from .mypaginations import MyPageNumberPagination
from .serializers import StudenSerializer
from .models import Student

# Create your views here.

# http://127.0.0.1:8000/api/studentapi/?mypage=2 for results
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudenSerializer
    pagination_class = MyPageNumberPagination
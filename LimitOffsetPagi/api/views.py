from rest_framework.generics import ListAPIView

from .mypaginations import MyLimitOffsetPagination
from .serializers import StudenSerializer
from .models import Student

# Create your views here.

# http://127.0.0.1:8000/api/studentapi/?limit=4&offset=5 (limit is per page view & offset is after 5 data)
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudenSerializer
    pagination_class = MyLimitOffsetPagination
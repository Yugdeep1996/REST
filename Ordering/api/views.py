from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

# http://127.0.0.1:8000/api/studentapi/?ordering=-id (- for desc)
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name', 'city']
    ordering_fields = ['name']


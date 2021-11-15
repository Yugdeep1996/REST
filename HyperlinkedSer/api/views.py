from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
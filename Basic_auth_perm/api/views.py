from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Student
from .serializers import StudentSerializer

# Create your views here.

# For crud operation
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Can be added globally in all functions via settings
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

 

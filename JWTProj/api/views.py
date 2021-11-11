from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer
# from .custom_auth import CustomAuthentication

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # http://127.0.0.1:8000/api/studentapi/?username=user1 <for custom auth>
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
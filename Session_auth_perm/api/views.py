from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,\
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .models import Student
from .serializers import StudentSerializer
# writing custom permissions
from .custom_permissions import MyPermission
# Create your views here.

# For crud operation
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Can be added globally in all functions via settings
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    # permission_classes = [DjangoModelPermissions]

 

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,\
    DestroyAPIView
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle

from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'


# from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# from .models import Student
# from .serializers import StudentSerializer
# from .throttling import JackRateThrottle

# # Create your views here.

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # http://127.0.0.1:8000/api/studentapi/?username=user1 <for custom auth>
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle, JackRateThrottle]
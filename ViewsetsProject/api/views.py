from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
# Normal Viewsets, ModelViewsets & ReadOnlyModelViewsets.

# For crud operation
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# For read only operation(List, retrieve)
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status 
# from rest_framework import viewsets

# from .models import Student
# from .serializers import StudentSerializer

# # Create your views here.

# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         print('List')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         print('Retreive')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         id=pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def create(self, request):
#         print('Create')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         print('Update')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         print('Partial')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Partial Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         print('destroy')
#         print('Basename',self.basename)
#         print('Action',self.action)
#         print('Detail',self.detail)
#         print('Suffix',self.suffix)
#         print('Name',self.name)
#         print('Description',self.description)
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             stu.delete()
#             return Response({'msg': 'Data Deleted'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
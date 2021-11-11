from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from .views import * 

# Create your urls here.

# router = DefaultRouter()

# router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('studentlist/', StudentList.as_view()),
    path('studentcreate/', StudentCreate.as_view()),
    path('studentretrieve/<int:pk>', StudentRetrieve.as_view()),
    path('studentupdate/<int:pk>', StudentUpdate.as_view()),
    path('studentdestroy/<int:pk>', StudentDestroy.as_view()),

    # path('', include(router.urls)), 
    # path('auth/', include('rest_framework.urls'), name='rest_framework'),
]

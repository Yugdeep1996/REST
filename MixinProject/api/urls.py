from django.urls import path
from .views import * 

# Create your views here.

urlpatterns = [
    path('studentlc/', StudentLC.as_view()),
    path('studentrud/<int:pk>', StudentRUD.as_view()),

    # path('studentlist/', StudentList.as_view()),
    # path('studentcreate/', StudentCreate.as_view()),
    # path('studentretrieve/<int:pk>', StudentRetrieve.as_view()),
    # path('studentupdate/<int:pk>', StudentUpdate.as_view()),
    # path('studentdestroy/<int:pk>', StudentDestroy.as_view()),
]
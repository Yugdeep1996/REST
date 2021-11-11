from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .auth import CustomAuthToken
from .views import * 

# Create your urls here.

router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')

# access token validity 5 mins.
# refresh token validity 1 day.

urlpatterns = [
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    path('gettoken/', TokenObtainPairView.as_view(), name="TokenObtainPairView"), 
    path('refreshtoken/', TokenRefreshView.as_view(), name="TokenRefreshView"),
    path('verifytoken/', TokenVerifyView.as_view(), name="TokenVerifyView"),
]

# using httpie.
# to send req at a link.
# http POST http://127.0.0.1:8000/api/gettoken/ username="user1" password="Admin@123" 
# http POST http://127.0.0.1:8000/api/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NjI4MjU2LCJpYXQiOjE2MzY2Mjc5NTYsImp0aSI6IjAxZTkwOWRlNGQxODQwZWE4MWRiMmQ4MzE4NjA1Mjg4IiwidXNlcl9pZCI6Mn0.JaFGk4JldAP0z79MV5x7iPepxhkaIya5NHldkHIwyEM"
# http POST http://127.0.0.1:8000/api/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjcxNDM1NiwiaWF0IjoxNjM2NjI3OTU2LCJqdGkiOiI5NzMxYTMxOTYzNWY0OTZmYTNiMTQ1N2FiZTdkMzkwYSIsInVzZXJfaWQiOjJ9.nQKIvfRoiZtsweULPVUnA6H_dwsx2s93Jn9XxOOGdB4"

# To get data
# http http://127.0.0.1:8000/api/studentapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NjI5NDY1LCJpYXQiOjE2MzY2Mjc5NTYsImp0aSI6IjM4NGVkMmFhODNmNjRhYzM4Y2E4ZDljNzczN2NmOTZkIiwidXNlcl9pZCI6Mn0.Q6tugL8pfOgImlk2QYIuwiXDSRkKwF2nJ8Xu_kLMiYY'
# To post data
# http -f POST http://127.0.0.1:8000/api/studentapi/ name=Raj roll=111 city=delhi 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NjI5ODQ2LCJpYXQiOjE2MzY2Mjc5NTYsImp0aSI6IjM4NzEwOWZlNzUzNzQyNjM5OTE0N2Q5MjdlYzFjMmU0IiwidXNlcl9pZCI6Mn0.4zg2FCb2SJP7FbdP-WVPSr10HYgITo7g-oAU731RUHw'
# To put data
#  http PUT http://127.0.0.1:8000/api/studentapi/5/ name=Raj roll=111 city=uk 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NjI5ODQ2LCJpYXQiOjE2MzY2Mjc5NTYsImp0aSI6IjM4NzEwOWZlNzUzNzQyNjM5OTE0N2Q5MjdlYzFjMmU0IiwidXNlcl9pZCI6Mn0.4zg2FCb2SJP7FbdP-WVPSr10HYgITo7g-oAU731RUHw'
# To delete data
#  http DELETE http://127.0.0.1:8000/api/studentapi/5/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NjI5ODQ2LCJpYXQiOjE2MzY2Mjc5NTYsImp0aSI6IjM4NzEwOWZlNzUzNzQyNjM5OTE0N2Q5MjdlYzFjMmU0IiwidXNlcl9pZCI6Mn0.4zg2FCb2SJP7FbdP-WVPSr10HYgITo7g-oAU731RUHw'
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

# http://127.0.0.1:8000/api/studentapi/?search=m for results
# to change search param see settings
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['name', 'city']
    search_fields = ['city']

# ^ starts-with search.
# = exact matches.
# @ full-text search (Postgres).
# $ regex search.

# eg :- search_fields = ['^city']
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'mypage'

    # http://127.0.0.1:8000/api/studentapi/?mypage=1&records=8 (for client input rec per page)
    page_size_query_param = 'records'

    max_page_size = 7
    last_page_strings = 'end'
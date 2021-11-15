from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name' # default is created
    cursor_query_param = 'cu' # default cursor
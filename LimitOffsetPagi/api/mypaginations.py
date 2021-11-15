from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 # can be overridden by user value
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 6
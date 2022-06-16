from rest_framework.pagination import CursorPagination, PageNumberPagination, LimitOffsetPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param="sayfa"
    
class LargePageNumberPagination(PageNumberPagination):
    page_size = 5

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'how_many'  # Defaults to 'limit'.

class MycursorPagination(CursorPagination):
    page_size=3
    ordering = "createdDate"
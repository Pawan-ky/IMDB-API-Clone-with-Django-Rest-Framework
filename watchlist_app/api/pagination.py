from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param  = 'size'
    max_page_size = 30        # restricting max page size
    # page_query_param='p'         # rename page with p
    
    
# limit offset paginantion
class WatchListLOPaginantion(LimitOffsetPagination):
    default_limit = 3
    max_limit = 30
    limit_query_param = 'limit'
    offset_query_param = 'start'   
    
# cursor paginantion
class WatchListCPagination(CursorPagination):
    page_size = 5 

    
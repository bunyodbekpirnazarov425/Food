from rest_framework.pagination import CursorPagination

class FoodTypePagination(CursorPagination):
    ordering = '-pk'
    
class FoodPagination(CursorPagination):
    ordering = '-pk'

class CommentPagination(CursorPagination):
    ordering = '-pk'
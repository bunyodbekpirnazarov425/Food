from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import ModelViewSet

from .models import FoodType, Food, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import FoodPagination, FoodTypePagination, CommentPagination

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .throttles import (FoodTypeAnonRateThrottle, FoodTypeUserRateThrottle,
                        FoodAnonRateThrottle,
                        FoodUserRateThrottle,
                        CommentAnonRateThrottle,
                        CommentUserRateThrottle)


def get_queryset(self):
    if self.request.version == 'v1':
        return Food.objects.all()
    else:
        return Food.objects.all()

def get_serializers_class(self):
    if self.request.version == 'v1':
        return FoodSerializer
    else:
        return FoodSerializer


class FoodTypeApiViewSet(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    throttle_classes = [FoodTypeAnonRateThrottle, FoodTypeUserRateThrottle, ScopedRateThrottle]
    throttle_scope = 'food_anon_detail'
    pagination_class = FoodTypePagination

class FoodApiViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    throttle_classes = [FoodAnonRateThrottle, FoodUserRateThrottle, ScopedRateThrottle]
    throttle_scope = 'food_anon_detail'
    pagination_class = FoodPagination

class CommentApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    throttle_classes = [CommentAnonRateThrottle, CommentUserRateThrottle, ScopedRateThrottle]
    throttle_scope = 'food_anon_detail'
    pagination_class = CommentPagination


# class FoodTypeListCreateView(GenericAPIView):
#     queryset = FoodType.objects.all()
#     serializer_class = FoodTypeSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     ordering_fields = ['name']
#
#     def get(self, request, *args, **kwargs):
#         food_types = self.get_queryset()
#         serializer = self.get_serializer(food_types, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class FoodListCreateView(GenericAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['name', 'composition']
#     ordering_fields = ['price']
#
#     def get(self, request, *args, **kwargs):
#         foods = self.get_queryset()
#         serializer = self.get_serializer(foods, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CommentListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['text']
#     ordering_fields = ['created']
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class FoodRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, mixins
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer

class FoodTypeListCreateView(GenericAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        food_types = self.get_queryset()
        serializer = self.get_serializer(food_types, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodListCreateView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        foods = self.get_queryset()
        serializer = self.get_serializer(foods, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



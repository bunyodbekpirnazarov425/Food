from django.urls import path, include
from .views import FoodTypeListCreateView, FoodListCreateView, CommentListCreateView, FoodRetrieveUpdateDestroyView

urlpatterns = [
    path('food-types/', FoodTypeListCreateView.as_view(), name='foodtype-list-create'),
    path('foods/', FoodListCreateView.as_view(), name='food-list-create'),
    path('foods/<int:pk>/', FoodRetrieveUpdateDestroyView.as_view(), name='food-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]

from django.urls import path, include
from .views import FoodTypeListCreateView, FoodListCreateView, CommentListCreateView

urlpatterns = [
    path('food-types/', FoodTypeListCreateView.as_view(), name='food-type-list-create'),
    path('foods/', FoodListCreateView.as_view(), name='food-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
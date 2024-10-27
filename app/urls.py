# from django.urls import path, include
from rest_framework import routers

from .views import (FoodTypeApiViewSet, FoodApiViewSet, CommentApiViewSet)

router = routers.SimpleRouter()
router.register('food-type', FoodTypeApiViewSet)
router.register('food', FoodApiViewSet)
router.register('comment', CommentApiViewSet)

urlpatterns = router.urls
from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=100)
    composition = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.food}'

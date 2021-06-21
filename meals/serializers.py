from rest_framework.serializers import ModelSerializer
from .models import Meal

class MealSerailizer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'author', 'price', 'date')
        model = Meal

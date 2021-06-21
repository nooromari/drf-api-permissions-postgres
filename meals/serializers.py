from rest_framework.serializers import ModelSerializer
from .models import Meal

class MealSerailizer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'chef', 'price', 'date')
        model = Meal

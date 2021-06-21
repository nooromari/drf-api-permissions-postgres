from django.urls import path
from .views import MealList, MealDetail


urlpatterns = [
    path("", MealList.as_view()),
    path("<int:pk>/", MealDetail.as_view()),
]

from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

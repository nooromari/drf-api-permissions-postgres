from django.db.models.aggregates import Count
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Meal


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a meal for the resturant menue 
        test_meal = Meal.objects.create(
          name="Shawerma", author=testuser1, price=2
        )
        test_meal.save()

    def test_blog_content(self):
        meal = Meal.objects.get(id=1)
        expected_author = f"{meal.author}"
        expected_name = f"{meal.name}"
        expected_price = meal.price
        self.assertEqual(expected_author, "testuser1")
        self.assertEqual(expected_name, "Shawerma")
        self.assertEqual(expected_price, 2)

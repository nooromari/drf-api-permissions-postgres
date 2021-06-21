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
          name="Shawerma", chef=testuser1, price=2
        )
        test_meal.save()

    def test_blog_content(self):
        meal = Meal.objects.get(id=1)
        expected_chef = f"{meal.chef}"
        expected_name = f"{meal.name}"
        expected_count = f"{meal.count}"
        self.assertEqual(expected_chef, "testuser1")
        self.assertEqual(expected_name, "Shawerma")
        self.assertEqual(expected_count, 2)

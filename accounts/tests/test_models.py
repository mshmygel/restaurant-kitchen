from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="john.doe",
            first_name="John",
            last_name="Doe"
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "jane.smith"
        years_of_experience = 10
        password = "gh61ha34"
        cook = get_user_model().objects.create_user(
            username=username,
            years_of_experience=years_of_experience,
            password=password
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))

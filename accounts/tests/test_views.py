
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="alice.jones",
            password="u1s2e3r4"
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "peter.pan",
            "password1": "zxzx1212",
            "password2": "zxzx1212",
            "first_name": "Peter",
            "last_name": "Pan",
            "years_of_experience": 8
        }
        self.client.post(reverse("accounts:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience, form_data["years_of_experience"]
        )

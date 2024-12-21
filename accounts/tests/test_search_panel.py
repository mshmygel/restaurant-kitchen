from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import Cook


class CookListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="nika.yer",
            password="fg56sd23vb78")
        self.client.force_login(self.user)

        self.cook1 = Cook.objects.create(
            username="fin.zevs",
            first_name="Finsar",
            last_name="Zevski",
            years_of_experience=2
        )
        self.cook2 = Cook.objects.create(
            username="hari.klin",
            first_name="Harry",
            last_name="Xander",
            years_of_experience=12
        )

    def test_search_cook_by_username(self):
        response = self.client.get(reverse("accounts:cook-list"),
                                   {"username": "fin.zevs"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fin.zevs")
        self.assertNotContains(response, "hari.klin")

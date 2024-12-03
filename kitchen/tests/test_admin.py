from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="user.tu",
            password="u1s2e3r4"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="moderator",
            password="z1x2c3v4",
            years_of_experience="20"
        )

    def test_cook_years_of_experience(self):
        """
        Test that chef's years of experience is in list_display on chef
        admin page
        :return:
        """

        url = reverse("admin:accounts_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience(self):
        """
        Test that chef's years of experience is on chef detail admin page
        :return:
        """

        url = reverse("admin:accounts_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

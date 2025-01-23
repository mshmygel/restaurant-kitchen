
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish_type-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="john.doe",
            password="u1s2e3r4"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Beverage")
        DishType.objects.create(name="Breakfast")

        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types),
        )
        self.assertTemplateUsed(
            response,
            "kitchen/dish_type_list.html"
        )

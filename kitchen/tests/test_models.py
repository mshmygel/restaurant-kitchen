from django.test import TestCase
from kitchen.models import Dish, DishType


class ModelTests(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        dish = Dish.objects.create(
            name="test",
            dish_type=dish_type,
            price=13.55
        )
        self.assertEqual(
            str(dish), f"{dish.name}, price: {dish.price}, description: {dish.description}"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Appetizer"
        )
        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}"
        )

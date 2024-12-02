from django.contrib import admin
from .models import DishType, Cook, Dish


admin.site.register(DishType)
admin.site.register(Cook)
admin.site.register(Dish)

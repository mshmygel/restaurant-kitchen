from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        null=False, blank=False, default=0
    )

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("accounts:cook-detail", kwargs={"pk": self.pk})

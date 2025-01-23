from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import Cook


class ExperienceValidationMixin:

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if years_of_experience < 0:
            raise ValidationError(
                "Value must be a positive number"
            )
        elif years_of_experience >= 50:
            raise ValidationError("Value must be less than 50")
        return years_of_experience


class CookCreationForm(ExperienceValidationMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "years_of_experience",
        )


class CookExperienceUpdateForm(ExperienceValidationMixin, forms.ModelForm):

    class Meta:
        model = Cook
        fields = ("years_of_experience",)


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


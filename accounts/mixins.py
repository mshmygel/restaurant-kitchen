from django.core.exceptions import ValidationError


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

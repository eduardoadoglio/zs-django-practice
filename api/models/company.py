from django.db import models

from api.models.language import Language


class Company(models.Model):
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timezone = models.CharField(max_length=50, default='-03:00')
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.PT
    )

    def get_language(self) -> Language:
        return Language[self.language]

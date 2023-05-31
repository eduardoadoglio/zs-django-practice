from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.TextChoices):
    PT = 'pt', _('Português')
    ES = 'es', _('Espanhol')
    EN = 'en', _('Inglês')
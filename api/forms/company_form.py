from django import forms
from django.utils.datetime_safe import time

from api.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nome', 'timezone', 'language']

from django import forms

from api.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nome', 'timezone', 'language']

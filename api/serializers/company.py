from rest_framework import serializers

from api.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['nome', 'timezone', 'language']
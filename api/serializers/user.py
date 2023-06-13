from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_email_verified = serializers.CharField(read_only=True)
    password_updated_at = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['email', 'is_email_verified', 'password', 'created_at', 'updated_at', 'password_updated_at']
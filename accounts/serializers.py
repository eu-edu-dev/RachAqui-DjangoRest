from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email', 'is_staff',
            'is_active', 'date_joined',
            'is_trusty', 'role'
        ]

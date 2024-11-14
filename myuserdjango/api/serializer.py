from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# Compare this snippet from myuserdjango/api/views.py:

    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be from example.com domain")
        return value
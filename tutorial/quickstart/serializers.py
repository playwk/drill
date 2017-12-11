from quickstart import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        field = ('user_name', 'user_info')
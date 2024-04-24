from rest_framework import serializers
from auth import models

"""序列化器"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "username",
            "password",
        )

    def to_representation(self, instance):
        data = {
            "id": instance.id,
            "username": instance.username,
            "password": instance.password,
        }
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            "avatar",
            "email",
            "phone",
            "steam_id",
        )

    def to_representation(self, instance):
        data = {
            "avatar": instance.avatar,
            "email": instance.email,
            "phone": instance.phone,
            "steam_id": instance.steam_id,
        }
        return data

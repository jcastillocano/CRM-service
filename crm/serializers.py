from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "photo")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user

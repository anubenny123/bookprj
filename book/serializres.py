from rest_framework import serializers
from django.contrib.auth.models import User
from book.models import Book

class Bookseializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password"

        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

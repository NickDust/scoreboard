from rest_framework import serializers
from .models import UserProfileModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfileModel
        fields = ['user', 'password', 'game_tag', 'points', 'premium', "rank"]

    def create(self, validated_data):
        game_tag = validated_data.pop("game_tag")
        password = validated_data.pop("password")
        points = validated_data.pop("points", 0)
        premium = validated_data.pop("premium", False)
        user_data = validated_data.pop("user")
        rank = validated_data.pop("rank")
        user = User.objects.create_user(username=user_data["username"], password=password)
        profile = UserProfileModel.objects.create(user=user, points=points, premium=premium, game_tag=game_tag)
        return profile
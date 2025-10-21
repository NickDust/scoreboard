from rest_framework import serializers
from registration.models import UserProfileModel
from registration.serializers import UserProfileSerializer

class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileModel
        field = ["points"]
        exclude = ["user", "game_tag", "premium"]

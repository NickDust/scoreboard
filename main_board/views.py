from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PointsSerializer
from registration.serializers import UserProfileSerializer
from django.shortcuts import get_object_or_404
from registration.models import UserProfileModel
from rest_framework.authentication import TokenAuthentication

class SubmissionPointsView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk):
        serializer = PointsSerializer(data=request.data)
        if serializer.is_valid():
            points = serializer.validated_data["points"]
            user = get_object_or_404(UserProfileModel, pk=pk)
            user.points += points
            user.save()
            return Response({"message": f"{points} points added. Total points {user.points}"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RankingView(APIView):
    def get(self, request):
        data = UserProfileModel.objects.all().order_by("-points")
        if not data:
            return Response({"message": "The ranking is empty"}, status=status.HTTP_404_NOT_FOUND)
        ranking = {}
        for user in data:
            points = user.points
            game_tag = user.game_tag
            rank = user.rank.rank if user.rank else None
            ranking[game_tag] = {"points": points,
                                 "Rank": rank}
        return Response({"ranking": [ranking]}, status=status.HTTP_200_OK)
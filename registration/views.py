from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfileModel
from .serializers import UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
            token, created = Token.objects.get_or_create(user=profile.user)
            return Response({"message": f"User({profile.user.username}) created successfully. game_tag: {profile.game_tag}",
                             "token": token.key}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
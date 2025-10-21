from rest_framework.views import APIView
from .models import LogModel
from rest_framework import status
from rest_framework.response import Response

class LogView(APIView):
    def get(self, request):
        try:
            data = {}
            logs = LogModel.objects.all()
            if not logs:
                return Response({"message": "No logs found"}, status=status.HTTP_404_NOT_FOUND)
            for log in logs:
                user = log.user.username
                entry = {
                    "action": log.action,
                    "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M")
                }
                if user not in data:
                    data[user] = []
                data[user].append(entry)
            return Response(data, status=status.HTTP_200_OK)
        except(ValueError, TypeError):
            return Response({"message": "Bad request, check the parameter or data format."}, status=status.HTTP_400_BAD_REQUEST)
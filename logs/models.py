from django.db import models
from django.contrib.auth.models import User

class LogModel(models.Model):
    
    ACTION = [
        ("USER_CREATED", "User created"),
        ("POINTS_ADDED", "Points added"),
        ("RANK_UP", "Rank up")
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50, choices=ACTION)
    timestamp = models.DateTimeField(auto_now_add=True)
    

from django.db import models

class RankModel(models.Model):
    rank = models.CharField(max_length=30)
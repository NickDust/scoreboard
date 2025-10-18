from django.db import models
from django.contrib.auth.models import User
from main_board.models import RankModel


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_tag = models.CharField(max_length=30, unique=True, blank=True)
    points = models.PositiveIntegerField(default=0)
    premium = models.BooleanField(default=False)
    rank = models.ForeignKey(RankModel, on_delete=models.PROTECT, null=True, blank=True)

    def rank_assignation(self):
        RANKS = [
            (0, 100, "Wood"),
            (101, 200, "Alluminium"),
            (201 , 400, "Iron"),
            (401, 600, "Gold"),
            (601, 800, "Emerald"),
            (801, 1500, "Not Human"),
            (1501, 2000, "Semi God"),
            (2001, 4000, "God"),
            (4001, 9999, "Who are You!?")
    ]
        for low, high, name in RANKS:
            if low <= self.points <= high:
                self.rank = RankModel.objects.get_or_create(rank=name)[0]
                break

    def game_tag_generator(self):
        import random
        import requests

        URL= "https://ddragon.leagueoflegends.com/cdn/15.20.1/data/en_US/champion.json"
        response = requests.get(URL)
        data = response.json()
        champion = random.choice(list(data['data'].keys()))
        random_number = random.randint(0, 999)
        return f"{self.user.username}The{champion}Rider{random_number}"
    
    def save(self, *args, **kwargs):
        if not self.game_tag or self.game_tag.strip() == "":
            tag = self.game_tag_generator()
            while UserProfileModel.objects.filter(game_tag=self.game_tag).exists():
                tag = self.game_tag_generator()
                self.game_tag = tag
        self.rank_assignation()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.game_tag} - {self.points} points" 


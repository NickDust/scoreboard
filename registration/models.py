from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_tag = models.CharField(max_length=30, unique=True, blank=True)
    points = models.PositiveIntegerField(default=0)
    premium = models.BooleanField(default=False)

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
        if not self.game_tag or self.game_tag == "":
            tag = self.game_tag_generator()
            while UserProfileModel.objects.filter(game_tag=self.game_tag).exists():
                tag = self.game_tag_generator()
                self.game_tag = tag
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.game_tag} - {self.points} points" 


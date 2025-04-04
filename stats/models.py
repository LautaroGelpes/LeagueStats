from django.db import models

from games.models import Game
from users.models import CommonUser


# Create your models here.
class Achievement(models.Model):
    user = models.ForeignKey(CommonUser, on_delete=models.CASCADE)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    #Creates the date automatically when the instance is created
    earned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.name}.'


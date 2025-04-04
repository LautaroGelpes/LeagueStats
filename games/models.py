from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100, unique=True, default='unknown Game')

    def __str__(self):
        return self.name

    @staticmethod
    def fetch_riot_games():
        """Obtiene los juegos de Riot Games y los guarda en la base de datos."""
        riot_games = ["League of Legends", "Valorant", "Teamfight Tactics", "Wild Rift", "Legends of Runeterra"]

        for game in riot_games:
            Game.objects.get_or_create(name=game)

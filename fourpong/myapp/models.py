from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class gameModel(models.Model):
  gamesWon = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.author) + " " + str(self.gamesWon)


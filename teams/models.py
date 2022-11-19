from django.db import models
from users.models import User

# Create your models here.

class Team(models.Model):
  team_name = models.CharField("team name", max_length=240)
  team_description = models.TextField()
  team_owner = models.OneToOneField(User, related_name='team_owner', on_delete=models.CASCADE)
  captains = models.ManyToManyField(User, related_name='team_captains')
  members = models.ManyToManyField(User, related_name='team_members')

from django.db import models

# Create your models here.


class Team(models.Model):
    # user must choose between preselected teams. they earn points for their team, and themselves
    # TEAMS = [
    #     ('kss', 'KryptSec'),
    #     ('hsh', 'hashdump'),
    #     ('mom', 'HackerMoms'),
    # ]
    team_name = models.CharField(max_length=20)
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name

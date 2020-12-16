from django.db import models

# Create your models here.

class Challenge(models.Model):

    challenge_name = models.CharField(max_length=30)
    difficulty = models.IntegerField(default=0)
    flag = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.challenge_name

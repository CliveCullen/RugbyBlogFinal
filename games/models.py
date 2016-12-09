from __future__ import unicode_literals
from django.db import models


# Create your models here.

class team(models.Model):
    Name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    rank = models.IntegerField()



    def __unicode__(self):
        return self.Name


class game(models.Model):
    date = models.DateField(blank=True, null=True)
    host = models.TextField()
    teamA = models.TextField()
    teamB = models.TextField()
    scoreA = models.IntegerField()
    scoreB = models.IntegerField()
    competition = models.TextField()

    def __unicode__(self):
        return self.host + " vs " + self.teamB + "  " +self.competition



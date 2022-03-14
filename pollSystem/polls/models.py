from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from datetime import datetime, timedelta


class Candidates(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=32)
    candidate_position = models.CharField(max_length=32)
    candidate_votes = models.IntegerField()

    def __str__(self):
        return str(self.candidate_name)


class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.position_name)


class Votes(models.Model):
    votes_id = models.AutoField(primary_key=True)
    voter_id = models.CharField(max_length=32, null=True)
    position = models.CharField(max_length=32, null=True)




# Create your models here.

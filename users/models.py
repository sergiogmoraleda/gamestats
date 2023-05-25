from django.db import models

# Create your models here.


class StatsUser(models.Model):

    id = models.AutoField(primary_key=True, serialize= True)
    wins = models.IntegerField(blank= True)
    defeat = models.IntegerField(blank= True)
    kda = models.TextField()
    headshotAccuracy = models.FloatField(blank= True)

class User(models.Model):

    id = models.AutoField(primary_key=True, serialize= True)
    username = models.TextField(blank= False)
    stats = models.ForeignKey(StatsUser, on_delete=models.CASCADE)

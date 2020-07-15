from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=30)
    team_id = models.IntegerField(primary_key=True)
    team_url = models.URLField()
    team_logo = models.URLField()

    class Meta:
        ordering = ['team_id']
    
    def __str__(self):
        return self.name

class Players(models.Model):
    name = models.CharField(max_length=30)
    photo = models.URLField()
    birthday = models.DateField(blank=True, null=True) 
    url = models.URLField() 
    player_id = models.IntegerField(primary_key=True)
    teams = models.ManyToManyField(Teams)
    name_score = models.IntegerField()

    class Meta:
        ordering = ['player_id']
    
    def __str__(self):
        return self.name + ' Name Score: ' + str(self.name_score)


                           
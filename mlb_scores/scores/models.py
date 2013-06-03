from django.db import models

# Create your models here.

class GamesSchedule(models.Model):

    game_date = models.DateField()
    game_id = models.CharField(max_length=12)
    espn_id = models.CharField(max_length=9)
    start_time_pdt = models.FloatField(blank=True, null=True) #Needs to be Float (timedelta)
    start_time_local = models.FloatField(blank=True, null=True) #Needs to be Float (timedelta)
    away = models.CharField(max_length=3)
    home = models.CharField(max_length=3)
    interleague = models.IntegerField()
    away_runs = models.IntegerField(null=True, blank=True)
    home_runs = models.IntegerField(null=True, blank=True)
    away_runs_5i = models.IntegerField(null=True, blank=True)
    home_runs_5i = models.IntegerField(null=True, blank=True)
    game_num = models.IntegerField(null=True, blank=True)
    game_status = models.CharField(max_length=16, null=True)


#CREATE TABLE games_schedule (
#game_date date NOT NULL,
#game_id char(12) NOT NULL,
#espn_id char(9) NOT NULL,
#start_time_pdt time,
#start_time_local time,
#away char(3) NOT NULL,
#home char(3) NOT NULL,
#interleague integer NOT NULL,
#away_runs integer,
#home_runs integer,
#away_runs_5i integer,
#home_runs_5i integer,
#game_num integer,
# game_status varchar(16)
#);

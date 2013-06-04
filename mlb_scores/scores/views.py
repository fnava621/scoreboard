from django.http import HttpResponse
from scores.models import GamesSchedule
from django.utils import simplejson
from django.core import serializers
import datetime


def home(request):
    dt = {"Hello": "World!"}
    jayson = simplejson.dumps(dt)
    return HttpResponse(jayson, mimetype='application/json')

def hours_minutes(td):
    td_str =  str(td.seconds//3600) + ":"\
                                    + str((td.seconds//60)%60)\
                                    + ':' +'0'
    std = datetime.datetime.strptime(td_str, '%H:%M:%S')
    time = std.strftime('%H:%M:%S')
    return time

def game_info(obj):
    start_time_pdt = datetime.timedelta(obj.start_time_pdt)
    start_time_local = datetime.timedelta(obj.start_time_local)
    matchup = {  
        'game_date' :obj.game_date.strftime('%Y-%m-%d'),
        'game_id': obj.game_id,
        'espn_id': obj.espn_id,
        'start_time_pdt': hours_minutes(start_time_pdt),
        'start_time_local': hours_minutes(start_time_local),
        'away': obj.away,
        'home': obj.home,
        'interleague': obj.interleague,
        'away_runs': obj.away_runs,
        'home_runs': obj.home_runs,
        'away_runs_5i': obj.away_runs_5i,
        'home_runs_5i': obj.home_runs_5i,
        'game_num': obj.game_num,
        'game_status': obj.game_status,
        } 
    
    return matchup
    
def date_games_info(request, date):
    Error_Response = HttpResponse("Invalid Date")
    try:
       make_date = datetime.datetime.strptime(date, '%Y%m%d')
       if type(make_date) != datetime.datetime:
           return Error_Response
    except:
        return Error_Response

    games_for_date = make_date.date()
    games = GamesSchedule.objects.filter(game_date=games_for_date)

    if games:
        data = {game.id:game_info(game) for game in games}
        jayson = simplejson.dumps(data)
        return HttpResponse(jayson, mimetype='application/json')
    else:
        try:
            game_date = games_for_date.strftime('%Y-%m-%d')
        except:
            return Error_Response
        return HttpResponse("No Games are available for %s" % game_date)


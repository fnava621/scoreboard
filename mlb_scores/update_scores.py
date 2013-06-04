import requests, datetime, os
from bs4 import BeautifulSoup
from scores.models import GamesSchedule

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return 

def update_mlb_scores():

    r = requests.get('http://scores.espn.go.com/mlb/scoreboard')
    soup = BeautifulSoup(r.text, 'html5lib')
    dt = (datetime.datetime.now() - datetime.timedelta(hours=3)).date()
    mlb_games = GamesSchedule.objects.filter(game_date=dt)

    for game in mlb_games:
        espn_game_id = game.espn_id
        status = soup.find(id=(espn_game_id + '-statusLine1'))

        if status:
            status = status.text
        else:
            staus = None

        game_in_progress = ['Bot', 'Mid', 'Top']
        inning_per = status.split()[0]

        if inning_per in game_in_progress:
            current_inning = int(filter(is_number, status))
        else:
            current_inning = None

        if status:
            print status
        if current_inning:
            print current_inning

        if current_inning:
            away_score = int(soup.find(id=(espn_game_id + '-alshT')).text)
            home_score = int(soup.find(id=(espn_game_id + '-hlshT')).text)
            game.away_runs = away_score
            game.home_runs = home_score
            game.game_status = status
            print away_score
            print home_score
            game.save()

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlb_scores.settings.production")
    update_mlb_scores()

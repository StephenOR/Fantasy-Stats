import urllib3
import json


def get_fantasy_data():
    http = urllib3.PoolManager()
    r = http.request('get', 'https://fantasy.premierleague.com/api/bootstrap-static/')

    a=json.loads(r.data)

    player_data_fpl = a['elements']

    return player_data_fpl

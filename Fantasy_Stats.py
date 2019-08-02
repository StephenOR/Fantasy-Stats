import asyncio
import json
import aiohttp
from Player import Player
import fpl_scraper
from Player_Lists import Player_Lists
from understat import Understat

async def get_understat_list_of_players():
    list_of_players = Player_Lists()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            "epl",
            2018,
        )
        for player in players:
            if '&#039;' in player.get('player_name'):
                player['player_name'] = player['player_name'].replace('&#039;' , "'")
            P = Player(player.get('player_name'), player.get('id'), int(player.get('goals')), int(player.get('assists')),
            float(player.get('xG')), float(player.get('xA')), float(player.get('npxG')), int(player.get('time')), int(player.get('games')),
            int(player.get('yellow_cards')), int(player.get('red_cards')))
            list_of_players.add_to_full_list(P)

    return list_of_players

def get_fpl_list_of_players():
    list_of_players = fpl_scraper.get_fantasy_data()
    return list_of_players

def match_data():
    fpl_list = get_fpl_list_of_players()
    for fpl_player in fpl_list:
        player_name = fpl_player.get('first_name') + ' ' + fpl_player.get('web_name')


def get_all_player_data():
    loop = asyncio.get_event_loop()
    understat_list_of_players = loop.run_until_complete(get_understat_list_of_players())
    fpl_player_data = get_fpl_list_of_players()
    for fpl_player in fpl_player_data:
        fpl_player_name = fpl_player.get('web_name')
        if fpl_player.get('first_name') != fpl_player.get('web_name'):
            fpl_player_name = fpl_player.get('first_name') + ' ' + fpl_player.get('web_name')
        found_player = understat_list_of_players.find_player_with_name(fpl_player_name)
        if found_player != None:
            found_player.set_fpl_value(fpl_player.get('now_cost'))
            found_player.set_fpl_points(fpl_player.get('total_points'))
            found_player.set_fpl_position(fpl_player.get('element_type'))
    return understat_list_of_players


a = get_all_player_data()
a.find_nofpl_players()

import asyncio
import json
import aiohttp
from Player import Player
import fpl_scraper
from Player_Lists import Player_Lists
from understat import Understat

async def get_understat_list_of_players():
    understat_list_of_players = []
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            "epl",
            2018
        )
        for player in players:
            if '&#039;' in player.get('player_name'):
                player['player_name'] = player['player_name'].replace('&#039;' , "'")
            understat_list_of_players.append(player)
    return understat_list_of_players

def get_fpl_list_of_players():
    list_of_players = Player_Lists()
    fpl_list = fpl_scraper.get_fantasy_data()
    newly_promoted_clubs = ["Norwich City", "Sheffield United", "Aston Villa"]
    for fpl_player in fpl_list:
        fpl_player_name = fpl_player.get('web_name')
        if fpl_player.get('first_name') != fpl_player.get('web_name'):
            fpl_player_name = fpl_player.get('first_name').split(' ') + ' ' + fpl_player.get('second_name')
            player_team = club_mapper(fpl_player.get('team'))
            if player_team in newly_promoted_clubs or fpl_player.get('total_points') == 0:
                P = Player(fpl_player_name, player_team, fpl_player.get('now_cost'), fpl_player.get('total_points'), fpl_player.get('element_type'),-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
            else:
                P = Player(fpl_player_name, player_team, fpl_player.get('now_cost'), fpl_player.get('total_points'), fpl_player.get('element_type'))
        list_of_players.add_to_full_list(P)
    return list_of_players

def get_all_player_data():
    loop = asyncio.get_event_loop()
    understat_list_of_players = loop.run_until_complete(get_understat_list_of_players())
    fpl_list_of_players = get_fpl_list_of_players()
    for understat_player in understat_list_of_players:
        found_player = fpl_list_of_players.find_player_with_name(understat_player.get('player_name'))
        if found_player != None:
            found_player.add_understat_values(understat_player.get('id'), understat_player.get('goals'), understat_player.get('assists'), understat_player.get('xG'),
            understat_player.get('xA'), understat_player.get('npxG'), understat_player.get('time'), understat_player.get('games'), understat_player.get('yellow_cards'), understat_player.get('red_cards'))
    return fpl_list_of_players

def club_mapper(club_id):
    club_dict = {1: 'Arsenal', 2: 'Aston Villa', 3: 'Bournemouth', 4: 'Brighton & Hove Albion', 5: 'Burnley', 6: 'Chelsea', 7: 'Crystal Palace',
    8: 'Everton', 9: 'Leicester City', 10: 'Liverpool', 11: 'Manchester City', 12: 'Manchester United', 13: 'Newcastle United', 14: 'Norwich City',
    15: 'Sheffield United', 16: 'Southampton', 17: 'Tottenham', 18: 'Watford', 19: 'West Ham', 20: 'Wolves'}
    return club_dict[club_id]


a = get_all_player_data()
a.find_nounderstat_players()

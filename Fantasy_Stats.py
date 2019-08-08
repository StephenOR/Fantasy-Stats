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

async def get_solo_player_data(understat_name, league):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            league,
            2018,
            player_name = understat_name
        )
        return players[0]


def get_fpl_list_of_players():
    list_of_players = Player_Lists()
    fpl_list = fpl_scraper.get_fantasy_data()
    for fpl_player in fpl_list:
        fpl_player_name = fpl_player.get('web_name')
        if fpl_player.get('first_name') != fpl_player.get('web_name'):
            fpl_player_name = fpl_player.get('first_name') + ' ' + fpl_player.get('second_name')
        player_team = club_mapper(fpl_player.get('team'))
        if fpl_player.get('total_points') == 0:
            P = Player(fpl_player_name, fpl_player.get('first_name'), fpl_player.get('second_name'), fpl_player.get('web_name'),
                player_team, fpl_player.get('now_cost'), fpl_player.get('total_points'), fpl_player.get('element_type'),fpl_player.get('clean_sheets'),fpl_player.get('bps'),-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
        else:
            P = Player(fpl_player_name, fpl_player.get('first_name'), fpl_player.get('second_name'), fpl_player.get('web_name'),
                player_team, fpl_player.get('now_cost'), fpl_player.get('total_points'), fpl_player.get('element_type'), fpl_player.get('clean_sheets'), fpl_player.get('bps'))
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
    fpl_list_of_players = get_transfered_player_data(fpl_list_of_players)
    return fpl_list_of_players

def get_transfered_player_data(player_list):
    transfered_players = {'Tanguy Ndombele' : ('Tanguy NDombele Alvaro', 'Ligue_1'), 'Rodri' : ('Rodri', 'La_Liga'), 'Nicolas Pépé' : ('Nicolas Pepe', 'Ligue_1'),
    'Daniel Ceballos Fernández' : ('Dani Ceballos', 'La_Liga'), 'Reiss Nelson' : ('Reiss Nelson', 'Bundesliga'), 'Erik Pieters' : ('Erik Pieters', 'Ligue_1'), 'Christian Pulisic' : ('Christian Pulisic', 'Bundesliga'),
    'Joelinton Cássio Apolinário de Lira' : ('Joelinton', 'Bundesliga'), 'Pablo Fornals' : ('Pablo Fornals', 'La_Liga'), 'Sébastien Haller' : ('Sébastien Haller', 'Bundesliga'), 'Jesús Vallejo Lázaro' : ('Jesús Vallejo', 'La_Liga'),
    'Patrick Cutrone' : ('Patrick Cutrone', 'Serie_A'), 'Moise Kean' : ('Moise Kean', 'Serie_A'), 'Allan Saint-Maximin' : ('Allan Saint-Maximin', 'Ligue_1'),  'Bjorn Engels' : ('Björn Engels', 'Ligue_1'),
    'Josip Drmic' : ('Josip Drmic', 'Bundesliga'), 'Ralf Fahrmann' : ('Ralf Fährmann', 'Bundesliga'), }
    #In the form of fpl name : Understat name, league name
    loop = asyncio.get_event_loop()
    for player in transfered_players:
        understat_player = loop.run_until_complete(get_solo_player_data(transfered_players[player][0],transfered_players[player][1]))
        found_player = player_list.find_player_with_name(player)
        if found_player != None:
            found_player.add_understat_values(understat_player.get('id'), understat_player.get('goals'), understat_player.get('assists'), understat_player.get('xG'),
            understat_player.get('xA'), understat_player.get('npxG'), understat_player.get('time'), understat_player.get('games'), understat_player.get('yellow_cards'), understat_player.get('red_cards'))
    return player_list


def club_mapper(club_id):
    club_dict = {1: 'Arsenal', 2: 'Aston Villa', 3: 'Bournemouth', 4: 'Brighton & Hove Albion', 5: 'Burnley', 6: 'Chelsea', 7: 'Crystal Palace',
    8: 'Everton', 9: 'Leicester City', 10: 'Liverpool', 11: 'Manchester City', 12: 'Manchester United', 13: 'Newcastle United', 14: 'Norwich City',
    15: 'Sheffield United', 16: 'Southampton', 17: 'Tottenham', 18: 'Watford', 19: 'West Ham', 20: 'Wolves'}
    return club_dict[club_id]


#Stats Analysis here onwards


def xPCalculator(list_of_players):
    output = []
    for player in list_of_players.get_full_list():
        output += (player.get_name(), player.NPxP_per_90())
    for i in output:
        print(i, '\n')

def xPToValueCaluclator(list_of_players):
    output = []
    for player in list_of_players.get_full_list():
        output += (player.get_name(), player.xPToValueCaluclator())
    for i in output:
        print(i , '\n')

def poisson(list_of_players):
    output = []
    for player in list_of_players.get_full_list():
        output += (player.get_name(), player.poisson_per_90())
    for i in output:
        print(i , '\n')

a = get_all_player_data()
for b in a.get_full_list():
    print(b)

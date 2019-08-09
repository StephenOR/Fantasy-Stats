import asyncio
import json
import aiohttp
from Player import Player
import fpl_scraper
from Player_Lists import Player_Lists
from understat import Understat
from Team import Team

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
    #Dictionary of % to take pens
    for understat_player in understat_list_of_players:
        found_player = fpl_list_of_players.find_player_with_name(understat_player.get('player_name'))
        if found_player != None:
            found_player.add_understat_values(understat_player.get('id'), understat_player.get('goals'), understat_player.get('assists'), understat_player.get('xG'),
            understat_player.get('xA'), understat_player.get('npxG'), understat_player.get('time'), understat_player.get('games'), understat_player.get('yellow_cards'), understat_player.get('red_cards'))
    fpl_list_of_players = get_transfered_player_data(fpl_list_of_players)
    fpl_list_of_players.find_penalty_takers()
    return fpl_list_of_players

def get_transfered_player_data(player_list):
    transfered_players = {'Tanguy Ndombele' : ('Tanguy NDombele Alvaro', 'Ligue_1'), 'Rodri' : ('Rodri', 'La_Liga'), 'Nicolas Pépé' : ('Nicolas Pepe', 'Ligue_1'),
    'Daniel Ceballos Fernández' : ('Dani Ceballos', 'La_Liga'), 'Reiss Nelson' : ('Reiss Nelson', 'Bundesliga'), 'Erik Pieters' : ('Erik Pieters', 'Ligue_1'), 'Christian Pulisic' : ('Christian Pulisic', 'Bundesliga'),
    'Joelinton Cássio Apolinário de Lira' : ('Joelinton', 'Bundesliga'), 'Pablo Fornals' : ('Pablo Fornals', 'La_Liga'), 'Sébastien Haller' : ('Sébastien Haller', 'Bundesliga'), 'Jesús Vallejo Lázaro' : ('Jesús Vallejo', 'La_Liga'),
    'Patrick Cutrone' : ('Patrick Cutrone', 'Serie_A'), 'Moise Kean' : ('Moise Kean', 'Serie_A'), 'Allan Saint-Maximin' : ('Allan Saint-Maximin', 'Ligue_1'),  'Bjorn Engels' : ('Björn Engels', 'Ligue_1'),
    'Josip Drmic' : ('Josip Drmic', 'Bundesliga'), 'Ralf Fahrmann' : ('Ralf Fährmann', 'Bundesliga'), 'João Pedro Cavaco Cancelo' : ('João Cancelo' , 'Serie_A')}
    #In the form of fpl name : Understat name, league name
    loop = asyncio.get_event_loop()
    for player in transfered_players:
        understat_player = loop.run_until_complete(get_solo_player_data(transfered_players[player][0],transfered_players[player][1]))
        found_player = player_list.find_player_with_name(player)
        if found_player != None:
            found_player.add_understat_values(understat_player.get('id'), understat_player.get('goals'), understat_player.get('assists'), understat_player.get('xG'),
            understat_player.get('xA'), understat_player.get('npxG'), understat_player.get('time'), understat_player.get('games'), understat_player.get('yellow_cards'), understat_player.get('red_cards'))
    return player_list

def generate_clubs(arsenal_ga,aston_villa_ga,bournemouth_ga,brighton_ga,burnley_ga,chelsea_ga,palace_ga,everton_ga,leicester_ga,liverpool_ga,mancity_ga,
                    united_ga,newcastle_ga,norwich_ga,sheffield_ga,southampton_ga, spurs_ga,watford_ga,westham_ga,wolves_ga):
                    list_of_clubs = []
                    list_of_clubs.append(Team("Arsenal",arsenal_ga))
                    list_of_clubs.append(Team("Aston Villa",aston_villa_ga))
                    list_of_clubs.append(Team("Bournemouth",bournemouth_ga))
                    list_of_clubs.append(Team("Brighton & Hove Albion",brighton_ga))
                    list_of_clubs.append(Team("Burnley",burnley_ga))
                    list_of_clubs.append(Team("Chelsea",chelsea_ga))
                    list_of_clubs.append(Team("Crystal Palace",palace_ga))
                    list_of_clubs.append(Team("Everton",everton_ga))
                    list_of_clubs.append(Team("Leicester City",leicester_ga))
                    list_of_clubs.append(Team("Liverpool",liverpool_ga))
                    list_of_clubs.append(Team("Manchester City",mancity_ga))
                    list_of_clubs.append(Team("Manchester United",united_ga))
                    list_of_clubs.append(Team("Newcastle United",newcastle_ga))
                    list_of_clubs.append(Team("Norwich City",norwich_ga))
                    list_of_clubs.append(Team("Sheffield United",sheffield_ga))
                    list_of_clubs.append(Team("Southampton",southampton_ga))
                    list_of_clubs.append(Team("Tottenham",spurs_ga))
                    list_of_clubs.append(Team("Watford",watford_ga))
                    list_of_clubs.append(Team("West Ham",westham_ga))
                    list_of_clubs.append(Team("Wolves",wolves_ga))
                    return list_of_clubs


def club_mapper(club_id):
    clubs_list = generate_clubs(57.30,66.50,62.42,62.46,66.12,38.11,52.80,49.31,44.64,29.15,25.73,52.30,57.55,73.59,67.19,59.27,49.15,63.29,65.66,42.69)
    club_dict = {1: clubs_list[0], 2: clubs_list[1], 3: clubs_list[2], 4: clubs_list[3], 5: clubs_list[4], 6: clubs_list[5], 7: clubs_list[6],
    8: clubs_list[7], 9: clubs_list[8], 10: clubs_list[9], 11: clubs_list[10], 12: clubs_list[11], 13: clubs_list[12], 14: clubs_list[13],
    15: clubs_list[14], 16: clubs_list[15], 17: clubs_list[16], 18: clubs_list[17], 19: clubs_list[18], 20: clubs_list[19]}
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
a.xP_Value_List(output_len = 25, min_mins = 900)

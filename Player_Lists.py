class Player_Lists:

    def __init__(self):
        self._full_list = []

    def __str__(self):
        outstr = ''
        for player in self._full_list:
            outstr += player.get_name()
            outstr += '\n'
        return outstr

    def get_full_list(self):
        return self._full_list

    def add_to_full_list(self,player):
        self._full_list.append(player)

    def find_player_with_name(self,name):
        unmatched_players = {'Joe Willock' : 'Joseph Willock', 'Mat Ryan' : 'Mathew Ryan', 'Solly March' : 'Solomon March', 'Ben Chilwell' : 'Benjamin Chilwell',
        'Caglar Söyüncü' : 'Çaglar Söyüncü', 'Diogo Dalot' : 'José Diogo Dalot Teixeira', 'Dele Alli' : 'Bamidele Alli', 'Romain Saiss' : 'Romain Saïss', 'Eddie Nketiah' : 'Edward Nketiah' }
        if name in unmatched_players:
            name = unmatched_players[name]
        for player in self._full_list:
            if player.get_name() == name:
                return player
            elif player.get_fpl_first_name().split(' ')[0] + ' ' + player.get_fpl_second_name().split(' ')[-1] == name:
                return player
            elif player.get_fpl_first_name().split(' ')[0] + ' ' + player.get_fpl_second_name().split(' ')[0] == name:
                return player
            elif player.get_fpl_web_name() == name:
                return player
            elif player.get_fpl_second_name() + ' ' + player.get_fpl_first_name() == name:
                return player
        return None

    def find_nounderstat_players(self):
        no_understat_players = []
        for player in self._full_list:
            if player.get_goals_18() == None:
                no_understat_players.append(player)
        return no_understat_players

    def find_no_stat_players(self):
        newly_promoted_clubs = ["Norwich City", "Sheffield United", "Aston Villa"]
        no_stat_players = []
        for player in self._full_list:
            if player.get_goals_18() == -1:
                no_stat_players.append(player)
                print(player)
        print(len(no_stat_players))
        return no_stat_players

    def find_duplicates(self):
        print(set([x for x in self._full_list if self._full_list.count(x._understat_ID) > 1]))

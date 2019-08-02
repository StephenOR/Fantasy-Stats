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
        for player in self._full_list:
            if player.get_name() == name:
                return player
        return None

    def find_nofpl_players(self):
        no_fpl_players = []
        for player in self._full_list:
            if player.get_fpl_value() == 0 or player.get_fpl_position() == 0:
                no_fpl_players.append(player)
                print(player,'\n')
        print (len(no_fpl_players))
        return no_fpl_players

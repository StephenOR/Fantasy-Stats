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
            if player.get_goals_18() == -1 and player.get_team() not in newly_promoted_clubs:
                no_stat_players.append(player)
                print(player)
        print(len(no_stat_players))
        return no_stat_players

    def find_duplicates(self):
        print(set([x for x in self._full_list if self._full_list.count(x._understat_ID) > 1]))

    def dictionary_printer(self,dictionary,max=1000):
        counter = 0
        for i in sorted(((v,k) for k,v in dictionary.items()), reverse=True):
            print(counter+1 , ' : ' , i)
            counter+=1
            if counter >= max:
                return

    def find_penalty_takers(self):
        penalty_dictionary = {'Pierre-Emerick Aubameyang' : 1, 'Alexandre Lacazette' : .1, 'Wesley Moraes' : 1, 'Jonathan Kodjia' : .1, 'Joshua King' : 1, 'Callum Wilson' : .1, 'Glenn Murray' : 1, 'Pascal Groß' :.1,
        'Chris Wood' : 1, 'Ashley Barnes' : .1, 'Ross Barkley' : .9, 'Tammy Abraham' : .2, 'Jorginho' : .15, 'Willian' : .1, 'Luka Milivojevic' : 1, 'Christian Benteke': .1, 'Gylfi Sigurdsson' : 1, 'Jamie Vardy' : 1, 'James Maddison' :.05,
        'James Milner' : 1, 'Mohamed Salah' : .8, 'Sergio Agüero' : 1, 'Gabriel Jesus' : .2, 'Paul Pogba' : 1, 'Marcus Rashford' : .1, 'Matt Ritchie' : 1, 'Miguel Almirón' : .1, 'Mario Vrancic' : 1, 'Teemu Pukki' : .1, 'Oliver Norwood' : 1,
        'David McGoldrick' : .1, 'Danny Ings' : 1, 'James Ward-Prowse' : .1, 'Harry Kane' : 1, 'Bamidele Alli' : .1, 'Troy Deeney' : 1, 'Tom Cleverley' : .1, 'Mark Noble' : 1, 'Sébastien Haller' : .1, 'Rúben Neves' : .7, 'Raúl Jiménez' : .3}
        for player_name in penalty_dictionary:
            found_player = self.find_player_with_name(player_name)
            if found_player != None:
                found_player.set_penalty_taker_chance(penalty_dictionary[player_name])
            else:
                print("ERROR ASSIGNING PEN TAKERS CAN'T FIND : %s" %player_name)

###Stats onwards

    def xP_List(self,positions = [1,2,3,4], output_len = 1000,min_mins = 450):
        output_dict = {}
        for player in self._full_list:
            if player.get_mins_18() == None or player.get_mins_18() < min_mins or player.get_fpl_position() not in positions:
                continue
            output_dict[player.get_name()] = (player.NPxP_per_90_calculator(), player.get_mins_18(), player.get_fpl_value())
        self.dictionary_printer(output_dict,output_len)

    def xP_Value_List(self,positions = [1,2,3,4], output_len = 1000,min_mins = 450):
        output_dict = {}
        for player in self._full_list:
            if player.get_mins_18() == None or player.get_mins_18() < min_mins or player.get_fpl_position() not in positions:
                continue
            output_dict[player.get_name()] = ((player.NPxP_per_90_calculator() / player.get_fpl_value()) *10, player.get_mins_18(), player.get_fpl_value())
        self.dictionary_printer(output_dict,output_len)

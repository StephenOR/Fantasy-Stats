class Player:

    def __init__(self,name, fpl_first_name, fpl_second_name, fpl_web_name, team, fpl_value, fpl_points, fpl_position, understat_ID = None,goals_18 = None,assists_18 = None,xG_18 = None,xA_18 = None,NPxG_18 = None,mins_18 = None,apps_18 = None,yellows_18 = None,reds_18 = None):
        self._name = name
        self._fpl_first_name = fpl_first_name
        self._fpl_second_name = fpl_second_name
        self._fpl_web_name = fpl_web_name
        self._team = team
        self._fpl_value = fpl_value
        self._fpl_points = fpl_points
        self._fpl_position = fpl_position
        self._understat_ID = understat_ID
        self._goals_18 = goals_18
        self._assists_18 = assists_18
        self._xG_18 = xG_18
        self._xA_18 = xA_18
        self._NPxG_18 = NPxG_18
        self._mins_18 = mins_18
        self._apps_18 = apps_18
        self._yellows_18 = yellows_18
        self._reds_18 = reds_18

    def __str__(self):
        output_str = "Name: %s\n" %self.get_name()
        output_str += "Team: %s\n" %self.get_team()
        output_str += "FPL Value: %i\n" %self.get_fpl_value()
        output_str += "FPL Points: %i\n" %self.get_fpl_points()
        output_str += "FPL Position: %i\n" %self.get_fpl_position()
        if self._goals_18 != None and self._goals_18 != -1 :
            output_str += "Goals 2018: %i\n" %self._goals_18
            output_str += "Assists 2018: %i\n" %self._assists_18
            output_str += "Expected Goals 2018: %f\n" %self._xG_18
            output_str += "Expected Assists 2018: %f\n" %self._xA_18
            output_str += "Non penalty xG 2018: %f\n" %self._NPxG_18
            output_str += "Mins played 2018: %i\n" %self._mins_18
            output_str += "Apps 2018: %i\n" %self._apps_18
            output_str += "Yellow Cards 2018: %i\n" %self._yellows_18
            output_str += "Red Cards 2018: %i\n" %self._reds_18

        return output_str

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_fpl_first_name(self):
        return self._fpl_first_name

    def set_fpl_first_name(self,fpl_first_name):
        self._fpl_first_name = fpl_first_name

    def get_fpl_second_name(self):
        return self._fpl_second_name

    def set_fpl_second_name(self,second_name):
        self._fpl_second_name = second_name

    def get_fpl_web_name(self):
        return self._fpl_web_name

    def set_fpl_web_name(self,fpl_web_name):
        self._fpl_web_name = fpl_web_name

    def get_team(self):
        return self._team

    def set_team(self,team):
        self._team = team

    def get_understat_ID(self):
        return self._understat_ID

    def set_understat_ID(self,understat_ID):
        self._understat_ID = int(understat_ID)

    def get_goals_18(self):
        return self._goals_18

    def set_goals_18(self,goals):
        self._goals_18 = int(goals)

    def get_assists_18(self):
        return self._assists_18

    def set_assists_18(self,assists):
        self._assists_18 = int(assists)

    def get_xG_18(self):
        return self._xG_18

    def set_xG_18(self,xG):
        self._xG_18 = float(xG)

    def get_xA_18(self):
        return self._xA_18

    def set_xA_18(self,xA):
        self._xA_18 = float(xA)

    def get_NPxG_18(self):
        return self._NPxG_18

    def set_NPxG_18(self,NPxG):
        self._NPxG_18 = float(NPxG)

    def get_mins_18(self):
        return self._mins_18

    def set_mins_18(self, mins):
        self._mins_18 = int(mins)

    def get_apps_18(self):
        return self._apps_18

    def set_apps_18(self,apps):
        self._apps_18 = int(apps)

    def get_yellows_18(self):
        return self._yellows_18

    def set_yellows_18(self,yellows):
        self._yellows_18 = int(yellows)

    def get_reds_18(self):
        return self._reds_18

    def set_reds_18(self,reds):
        self._reds_18 = int(reds)

    def get_fpl_value(self):
        return self._fpl_value

    def set_fpl_value(self,value):
        self._fpl_value = value

    def get_fpl_position(self):
        return self._fpl_position

    def set_fpl_position(self,position):
        self._fpl_position = position

    def get_fpl_points(self):
        return self._fpl_points

    def set_fpl_points(self,points):
        self._fpl_points = points

    def get_per90_xG(self):
        xG = self.get_xG_18() * 90
        xG = xG / self._mins_18()
        return xG

    def get_per90_NPxG(self):
        NPxG = self.get_NPxG_18() * 90
        NPxG = NPxG / self.get_mins_18()
        return NPxG

    def get_per90_xA(self):
        xA = self.get_xA_18() * 90
        xA = xA / self.get_mins_18()
        return xA

    def NPxP_per_90(self):
        player_position = self.get_fpl_position()
        player_xp = 0
        if player_position == 1:
            return 0
        elif player_position == 2:
            player_xp += self.get_per90_NPxG() * 6
            player_xp += self.get_per90_xA() * 3
        elif player_position == 3:
            player_xp += self.get_per90_NPxG() * 5
            player_xp += self.get_per90_xA() * 3
        else:
            player_xp += self.get_per90_NPxG() * 4
            player_xp += self.get_per90_xA() * 3
        return player_xp

    def get_NPxP_to_value(self):
        player_NPxP_p90 = self.NPxP_per_90()
        NPxP_val = player_NPxP_p90 / player.get_fpl_value()
        return NPxP_val


    def add_understat_values(self,id,goals_18,assists_18,xG_18,xA_18,NPxG_18,mins_18,apps_18,yellows_18,reds_18):
        self.set_understat_ID(id)
        self.set_goals_18(goals_18)
        self.set_assists_18(assists_18)
        self.set_xG_18(xG_18)
        self.set_xA_18(xA_18)
        self.set_NPxG_18(NPxG_18)
        self.set_mins_18(mins_18)
        self.set_apps_18(apps_18)
        self.set_yellows_18(yellows_18)
        self.set_reds_18(reds_18)


def main():
    eh = Player("Eden", 110, 111, 112, 113, 114, 115, 116, 117, 118, 119)
    print(eh.get_reds_18())

if __name__ == "__main__":
    main()

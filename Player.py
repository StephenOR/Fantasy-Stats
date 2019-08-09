class Player:

    def __init__(self,name, fpl_first_name, fpl_second_name, fpl_web_name, team, fpl_value, fpl_points, fpl_position, fpl_clean_sheets, fpl_bps, understat_ID = None,goals_18 = None,assists_18 = None,xG_18 = None,xA_18 = None,XGI_18 = None,NPxG90 = None,xA90 = None,xG90 = None,xGI90 = None,NPxGI90 = None,NPxG_18 = None,mins_18 = None,apps_18 = None,yellows_18 = None,reds_18 = None,penalty_taker_chance = 0):
        self._name = name
        self._fpl_first_name = fpl_first_name
        self._fpl_second_name = fpl_second_name
        self._fpl_web_name = fpl_web_name
        self._team = team
        self._fpl_bps = fpl_bps
        self._fpl_value = fpl_value
        self._fpl_points = fpl_points
        self._fpl_clean_sheets = fpl_clean_sheets
        self._fpl_position = fpl_position
        self._understat_ID = understat_ID
        self._goals_18 = goals_18
        self._assists_18 = assists_18
        self._xG_18 = xG_18
        self._xA_18 = xA_18
        self._XGI_18 = XGI_18
        self._NPxG_18 = NPxG_18
        self._NPxG90 = NPxG90
        self._xG90 = xG90
        self._xA90 = xA90
        self._xGI90 = xGI90
        self._NPxGI90 = NPxGI90
        self._mins_18 = mins_18
        self._apps_18 = apps_18
        self._yellows_18 = yellows_18
        self._reds_18 = reds_18
        self._penalty_taker_chance = penalty_taker_chance

    def __str__(self):
        output_str = "Name: %s\n" %self.get_name()
        output_str += "Team: %s\n" %self.get_team().get_name()
        output_str += "FPL Value: %i\n" %self.get_fpl_value()
        output_str += "FPL Points: %i\n" %self.get_fpl_points()
        output_str += "FPL Position: %i\n" %self.get_fpl_position()
        output_str += "Clean Sheets: %i\n" %self.get_fpl_clean_sheets()
        output_str += "Bonus Points: %i\n" %self.get_fpl_bps()
        if self._goals_18 == None or self._goals_18 == -1 :
            return output_str
        else :
            output_str += "REAL DATA: ########################\n"
            output_str += "Mins played 2018: %i\n" %self._mins_18
            output_str += "Apps 2018: %i\n" %self._apps_18
            output_str += "Goals 2018: %i\n" %self._goals_18
            output_str += "Assists 2018: %i\n" %self._assists_18
            output_str += "EXPECTED DATA: ####################\n"
            output_str += "Expected Goals 2018: %f\n" %self._xG_18
            output_str += "Expected Assists 2018: %f\n" %self._xA_18
            output_str += "Non penalty xG 2018: %f\n" %self._NPxG_18
            output_str += "PER 90 DATA: ######################\n"
            output_str += "Expected goals per 90 %f\n" %self._xG90
            output_str += "Expected Non penalty goals per 90 %f\n" %self._NPxG90
            output_str += "Expected Assists per 90 %f\n" %self._xA90
            output_str += "Expected goal involvments per 90 %f\n" %self._xGI90
            output_str += "Non-Pen expected goal invovlements per 90 %f\n" %self._NPxGI90
            if self.get_penalty_taker_chance() > 0:
                output_str += "Penalty taker chance: %f\n" %self._penalty_taker_chance
        return output_str



    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_fpl_bps(self):
        return self._fpl_bps

    def set_fpl_bps(self,fpl_bps):
        self._fpl_bps = fpl_bps

    def get_fpl_clean_sheets(self):
        return self._fpl_clean_sheets

    def set_fpl_clean_sheets(self,clean_sheets):
        self._fpl_clean_sheets = clean_sheets

    def set_name(self,fpl_clean_sheets):
        self._fpl_clean_sheets = fpl_clean_sheets

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
        self._fpl_value = int(value)

    def get_fpl_position(self):
        return self._fpl_position

    def set_fpl_position(self,position):
        self._fpl_position = int(position)

    def get_fpl_points(self):
        return self._fpl_points

    def set_fpl_points(self,points):
        self._fpl_points = int(points)

    def get_XGI_18(self):
        return self._XGI_18

    def set_XGI_18(self):
        self._XGI_18 = self.get_xG_18() + self.get_xA_18()

    def get_penalty_taker_chance(self):
        return self._penalty_taker_chance

    def set_penalty_taker_chance(self,chance):
        self._penalty_taker_chance = chance

    def get_NPxG90(self):
        return self._NPxG90

    def set_NPxG90(self):
        self._NPxG90 = float((90 * self.get_NPxG_18()) / self.get_mins_18())

    def get_xG90(self):
        return self._xG90

    def set_xG90(self):
        self._xG90 = float((90 * self.get_xG_18() / self.get_mins_18()))

    def get_xA90(self):
        return self._xA90

    def set_xA90(self):
        self._xA90 = float(90 * self.get_xA_18() / self.get_mins_18())

    def get_xGI90(self):
        return self._xGI90

    def set_xGI90(self):
        self._xGI90 = float(self.get_xG90() + self.get_xA90())

    def get_NPxGI90(self):
        return self._NPxGI90

    def set_NPxGI90(self):
        self._NPxGI90 = float(self.get_NPxG90() + self.get_xA90())

    def NPxP_per_90_calculator(self):
        player_position = self.get_fpl_position()
        player_xp = 2
        team = self.get_team()
        poisson_per_90 = team.poisson_per_90()
        pen_taker = False
        if self.get_penalty_taker_chance() > 0:
            pen_taker = True
        if player_position == 1:
            #Poisson is for cleansheets
            player_xp += poisson_per_90[0]
        elif player_position == 2:
            player_xp += poisson_per_90[0]
            player_xp += self.get_NPxG90() * 6
            player_xp += self.get_xA90() * 3
            if pen_taker:
                player_xp += .4 * self.get_penalty_taker_chance()
        elif player_position == 3:
            player_xp += poisson_per_90[1]
            player_xp += self.get_NPxG90() * 5
            player_xp += self.get_xA90() * 3
            if pen_taker:
                player_xp += .325 * self.get_penalty_taker_chance()
        else:
            player_xp += self.get_NPxG90() * 4
            player_xp += self.get_xA90() * 3
            if pen_taker:
                player_xp += .25 * self.get_penalty_taker_chance()
        return player_xp

    def get_NPxP_to_value_calculator(self):
        player_NPxP_p90 = self.NPxP_per_90()
        NPxP_val = player_NPxP_p90 / player.get_fpl_value()
        return NPxP_val

    def bonus_score_expected_difference(self):
        player_position = self.get_fpl_position()
        player_expected_bps = 0
        player_bps = self.get_fpl_bps()
        euler_to_minus_lambda = math.exp(0-team_xGA_per_90)
        player_clean_sheets = self.get_fpl_clean_sheets()
        if player_position == 1:
            player_expected_bps = 12*(38*euler_to_minus_lambda-player_clean_sheets)+player_bps


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
        self.set_NPxG90()
        self.set_xA90()
        self.set_xG90()
        self.set_XGI_18()
        self.set_xGI90()
        self.set_NPxGI90()



def main():
    eh = Player("Eden", 110, 111, 112, 113, 114, 115, 116, 117, 118, 119)
    eh.set_fpl_position(2)
    eh.NPxP_per_90_calculator()

if __name__ == "__main__":
    main()

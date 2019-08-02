class Player:

    def __init__(self,name,understat_ID,goals_18,assists_18,xG_18,xA_18,NPxG_18,mins_18,apps_18,yellows_18,reds_18):
        self._name = name
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
        self._fpl_value = 0
        self._fpl_points = 0
        self._fpl_position = 0

    def __str__(self):
        output_str = "Name : %s\n" %self._name
        output_str += "Goals 2018: %i\n" %self._goals_18
        output_str += "Assists 2018: %i\n" %self._assists_18
        output_str += "Expected Goals 2018: %f\n" %self._xG_18
        output_str += "Expected Assists 2018: %f\n" %self._xA_18
        output_str += "Non penalty xG 2018: %f\n" %self._NPxG_18
        output_str += "Mins played 2018: %i\n" %self._mins_18
        output_str += "Apps 2018: %i\n" %self._apps_18
        output_str += "Yellow Cards 2018: %i\n" %self._yellows_18
        output_str += "Red Cards 2018: %i\n" %self._reds_18
        output_str += "FPL Value: %i\n" %self._fpl_value
        output_str += "FPL Points: %i\n" %self._fpl_points
        output_str += "FPL Position: %i" %self._fpl_position
        return output_str

    def get_name(self):
        return self._name

    def get_understat_ID(self):
        return self._understat_ID

    def get_goals_18(self):
        return self._goals_18

    def get_assists_18(self):
        return self._assists_18

    def get_xG_18(self):
        return self._xG_18

    def get_xA_18(self):
        return self._xA_18

    def get_NPxG_18(self):
        return self._NPxG_18

    def get_mins_18(self):
        return self._mins_18

    def get_apps_18(self):
        return self._apps_18

    def get_yellows_18(self):
        return self._yellows_18

    def get_reds_18(self):
        return self._reds_18

    def get_fpl_value(self):
        return self._fpl_value

    def get_fpl_position(self):
        return self._fpl_position

    def get_fpl_points(self):
        return self._fpl_points

    def set_fpl_value(self,value):
        self._fpl_value = value

    def set_fpl_position(self,position):
        self._fpl_position = position

    def set_fpl_points(self,points):
        self._fpl_points = points

def main():
    eh = Player("Eden", 110, 111, 112, 113, 114, 115, 116, 117, 118, 119)
    print(eh.get_reds_18())

if __name__ == "__main__":
    main()

import math
class Team:

    def __init__ (self,name,xGA,games_played=38):
        self._name = name
        self._xGA = xGA
        self._games_played = games_played

    def __str__(self):
        outputstr = "Team Name: %s\n" %self.get_name()
        outputstr += "Games Played: %i" %self.get_games_played()
        outputstr += "Non penalty xGA: %f" %self.get_xGA()
        outputstr += "Poisson Per 90: %f" %self.get_poisson_per_90()
        return outputstr

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_xGA(self):
        return self._xGA

    def set_xGA(self,xGA):
        self._xGA = xGA

    def get_games_played(self):
        return self._games_played

    def set_games_played(self,games_played):
        self._games_played = games_played

    def poisson_per_90(self):
        team_xGA_per_90 = self.get_xGA() / self.get_games_played()
        k=2
        euler_to_minus_lambda = math.exp(0-team_xGA_per_90)
        midfielder_addition = euler_to_minus_lambda
        defender_or_goalkeeper_addition = 0
        defender_or_goalkeeper_addition = 4*euler_to_minus_lambda
        while k<4:
            defender_or_goalkeeper_addition-=((euler_to_minus_lambda)*(team_xGA_per_90**k))/math.factorial(k)
            k+=1
        while k<6:
            defender_or_goalkeeper_addition-=2*((euler_to_minus_lambda)*(team_xGA_per_90**k))/math.factorial(k)
            k+=1
        while k<8:
            defender_or_goalkeeper_addition-=3*((euler_to_minus_lambda)*(team_xGA_per_90**k))/math.factorial(k)
            k+=1
        return(defender_or_goalkeeper_addition,midfielder_addition)

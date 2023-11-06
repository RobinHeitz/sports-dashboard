from enum import Enum, EnumMeta
from pydantic import BaseModel
import datetime

from typing import Optional, List


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class HandballTeamsBundesliga(str, Enum, metaclass=MetaEnum):
    berlin = "Füchse Berlin"
    scm = "SC Magdeburg"
    melsungen = "MT Melsungen"
    flensbug = "SG Flensburg-Handewitt"
    kiel = "THW Kiel"
    vfl = "VfL Gummersbach"
    loewen = "Rhein-Neckar Löwen"
    hannover = "TSV Hannover-Burgdorf"
    leipzig = "SC DHfK Leipzig"
    hamburg = "Handball Sport Verein Hamburg"
    bhc = "Bergischer HC"
    erlangen = "HC Erlangen"
    stuttgart = "TVB Stuttgart"
    lemgo = "TBV Lemgo Lippe"
    goeppingen = "FRISCH AUF! Göppingen"
    eisenach = "ThSV Eisenach"
    wetzlar = "HSG Wetzlar"
    balingen = "HBW Balingen-Weilstetten"


class HandballTeamsChampionsLeague(str, Enum, metaclass=MetaEnum):
    scm = "SC Magdeburg"
    gog = "GOG"
    zagreb = "HC Zagreb"
    kielce = "Industria Kielce"
    szeged = "OTP Bank - PICK Szeged"
    pelister = "HC Eurofarm Pelister"
    thw = "THW Kiel"
    aalbord = "Aalborg Håndbold"
    montpellier = "Montpellier HB"
    porto = "FC Porto"
    kolstad = "Kolstad Handball"
    psg = "Paris Saint-Germain Handball"
    celje = "RK Celje Pivovarna Laško"
    veszprem = "Telekom Veszprém HC"
    barca = "Barça"
    plock = "Orlen Wisla Plock"
    
class MatchStats:
    team_name: str = ''
    matches_won: int = 0
    matches_lost: int = 0
    matches_drawn: int = 0
    games_played: int = 0
    goals_scored: int = 0
    goals_conceded: int = 0

    def __init__(self, team_name):
        self.team_name = team_name

    def __str__(self):
        return f'{self.team_name} {self.matches_won=} {self.matches_lost=}'

    def __repr__(self):
        return f'{self.team_name} {self.matches_won=} {self.matches_lost=}'


    def inc_games_played(self):
        self.games_played += 1

    def inc_wins(self):
        self.matches_won += 1

    def inc_losses(self):
        self.matches_lost += 1

    def inc_draws(self):
        self.matches_drawn += 1

    def add_goals_scored(self, goals):
        self.goals_scored += goals

    def add_goals_conceded(self, goals):
        self.goals_conceded += goals

    @property
    def goal_ratio(self):
        return self.goals_scored - self.goals_conceded
    
    @property
    def points(self):
        return self.matches_won * 2 + self.matches_drawn




class Match(BaseModel):

    class Config:
        use_enum_values = True

    start_time: datetime.time
    home_team: HandballTeamsBundesliga | HandballTeamsChampionsLeague
    away_team: HandballTeamsBundesliga | HandballTeamsChampionsLeague

    already_played: bool = False
    home_goals: Optional[int] = 0
    away_goals: Optional[int] = 0

    def home_team_won(self):
        return self.home_goals > self.away_goals

    def away_team_won(self):
        return self.away_goals > self.home_goals

    def draw_game(self):
        return self.away_goals == self.home_goals and self.already_played == True


class ScheduledGameday(BaseModel):
    date: datetime.date
    matches: List[Match]

    def __str__(self):
        goals = sum(match.home_goals for match in self.matches) + sum(match.away_goals for match in self.matches)
        if goals > 0:
            avg = round(goals / len(self.matches) / 2,1)
            return f"Gameday: {self.date} with {len(self.matches)} matches with a total of {goals} goals (avg. per team = {avg})."
        return f"Gameday: {self.date} with {len(self.matches)} matches."
    


if __name__ == "__main__":

    test1 = "GOS"
    print(test1 in HandballTeamsChampionsLeague)

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
    


class Match(BaseModel):

    class Config:
        use_enum_values = True

    start_time: datetime.time
    home_team: HandballTeamsBundesliga | HandballTeamsChampionsLeague
    away_team: HandballTeamsBundesliga | HandballTeamsChampionsLeague

    already_played: bool = False
    home_goals: Optional[int] = 0
    away_goals: Optional[int] = 0


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
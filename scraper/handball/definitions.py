import enum
from pydantic import BaseModel
import datetime

from typing import Optional, List


class HandballTeamsBundesliga(str, enum.Enum):
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


class HandballTeamsChampionsLeague(str, enum.Enum):
    pass


class GamePairing(BaseModel):

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
    matches: List[GamePairing]

    def __str__(self):
        goals = sum(match.home_goals for match in self.matches) + sum(match.away_goals for match in self.matches)
        if goals > 0:
            avg = round(goals / len(self.matches) / 2,1)
            return f"Gameday: {self.date} with {len(self.matches)} matches with a total of {goals} goals (avg. per team = {avg})."
        return f"Gameday: {self.date} with {len(self.matches)} matches."
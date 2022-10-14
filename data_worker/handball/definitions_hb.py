from datetime import datetime
from typing import List, Protocol, Tuple, Optional
from enum import Enum

from pydantic import BaseModel, Field, root_validator


class HandballStageEnum(str, Enum):
    """Enum for Football Stage like if it's Regular Season or group stage of some cup."""
    REGULAR_SEASON = "REGULAR_SEASON" 
    GROUP_STAGE = "GROUP_STAGE"

class HandballTypeEnum(str, Enum):
    """Football Standings Type, like total standings or just home (or away)."""
    TOTAL = "TOTAL"
    HOME = "HOME"
    AWAY = "AWAY"



class HandballStanding(BaseModel):
    """Standing of a league, containing a list of HandballPosition - Elements."""
    competition_name: str
    table: List["HandballPosition"]
    type: str = HandballTypeEnum
    stage: str = HandballStageEnum


class HandballPosition(BaseModel):
    """Standing of a particular handball team in specific competition."""
    position: int
    team:str
    played_games: str
    won:int
    draw:int
    lost:int
    points: str
    goal_difference:int
    goals_for: int
    goals_against:int

    @classmethod
    def get_table_columns(cls) -> Tuple[str]:
        return ("Position", "Team", "Spiele", "Sieg", "Unentschieden", "Niederlage", "Punkte", "Differenz", "Tore erzielt", "Tore kassiert")

    
    def get_rows(self) -> Tuple[str]:
        return (
            str(self.position),
            str(self.team),
            str(self.played_games),
            str(self.won),
            str(self.draw),
            str(self.lost),
            str(self.points),
            str(self.goal_difference),
            str(self.goals_for),
            str(self.goals_against),
        )

HandballStanding.update_forward_refs()

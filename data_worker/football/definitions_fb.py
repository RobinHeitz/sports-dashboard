from datetime import datetime
from typing import List, Protocol, Tuple, Optional
from dataclasses import dataclass
from random import choices, randint
from enum import Enum, auto

from pydantic import BaseModel, Field, root_validator



class FootballStageEnum(str, Enum):
    """Enum for Football Stage like if it's Regular Season or group stage of some cup."""
    REGULAR_SEASON = "REGULAR_SEASON" 
    GROUP_STAGE = "GROUP_STAGE"

class FootballTypeEnum(str, Enum):
    """Football Standings Type, like total standings or just home (or away)."""
    TOTAL = "TOTAL"
    HOME = "HOME"
    AWAY = "AWAY"


class FootballStanding(BaseModel):
    """Standings of a competition like Bundesliga or UEFA Champions League."""
    stage: FootballStageEnum
    type: FootballTypeEnum
    group: Optional[str]
    table: List["FootballPosition"] = Field(..., alias="table")


class FootballPosition(BaseModel):
    """Standing of a particular team in a given competition"""
    position: int
    team: str
    played_games: int = Field(..., alias="playedGames")
    won:int
    draw:int
    lost:int
    points: int
    goals_for: int  = Field(..., alias="goalsFor")
    goals_against:int = Field(..., alias="goalsAgainst")
    goal_difference:int = Field(..., alias="goalDifference")

    @root_validator(pre=True)
    def flatten_data_structure(cls, values):
        team = values.pop("team")
        return {**values, "team": team.get("name")}

    
    @classmethod
    def get_table_columns(cls) -> Tuple[str]:
        return ("Position", "Team", "Spiele", "Sieg", "Unentschieden", "Niederlage", "Punkte", "Tore erzielt", "Tore kassiert", "Differenz")

    
    def get_rows(self) -> Tuple[str]:
        return (
            str(self.position),
            str(self.team),
            str(self.played_games),
            str(self.won),
            str(self.draw),
            str(self.lost),
            str(self.points),
            str(self.goals_for),
            str(self.goals_against),
            str(self.goal_difference),
        )



FootballStanding.update_forward_refs()

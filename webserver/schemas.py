from datetime import datetime
from typing import List, Protocol, Tuple, Optional
from enum import Enum

from pydantic import BaseModel

class CompetitionStage(str, Enum):
    """Competition's stage definition."""
    REGULAR_SEASON = "REGULAR_SEASON"
    GROUP_STAGE = "GROUP_STAGE"


class Competition(BaseModel):
    """Represents a competition."""
    competition_name: str
    stage: CompetitionStage
    standing: "Standing"

    class Config:
        orm_mode = True

class Standing(BaseModel):
    """Represents the current standing of teams within its competition."""
    positions: List["Position"]
    updated: datetime

    class Config:
        orm_mode = True

class Position(BaseModel):
    """Standing of a team within its connected competition."""
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

    class Config:
        orm_mode = True

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



Standing.update_forward_refs()
Competition.update_forward_refs()
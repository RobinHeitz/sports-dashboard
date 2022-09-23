from datetime import datetime
from typing import List, Protocol, Tuple
from dataclasses import dataclass
from random import choices, randint
from enum import Enum, auto

class DashboardType(Enum):
    gameday = auto()
    placement_table = auto()

class SportsType(Enum):
    soccer = auto()
    handball = auto()




class GameItem(Protocol):
    def output_table_row(self) -> Tuple[str]:
        """Returns tuple of attributes of this instance. Number of items within tuple need to match the number of items from get_columns()."""

    def get_columns():
        """Returns list of dictionarys with attributes that define how the column-headers should be displayed."""



@dataclass
class DashboardItem:
    """Item representing a set of data, like current bundeliga spieltag or current table of UEFA CL."""
    title: str
    sports_type: SportsType
    dashboard_type: DashboardType
    game_items: List[GameItem]




@dataclass
class GameResult:
    """Represents a game between 2 teams."""
    date: datetime
    home_team: str
    opposing_team: str
    home_goals: int
    opposing_goals: int

    @classmethod
    def get_columns(cls) -> List[dict]:
        """Returns list of dictionarys with attributes that define how the column-headers should be displayed."""
        return [
            dict(header="Date", justify="center", style="cyan"),
            dict(header="Home Team", justify="center", style="blue"),
            dict(header="Opposing Team", justify="center", style="yellow"),
            dict(header="Result", justify="center", style="red"),
        ]

    def output_table_row(self) -> Tuple[str]:
        """Returns tuple of attributes of this instance. Number of items within tuple need to match the number of items from get_columns()."""
        return (
            self.date.strftime("%a, %d. %b %y - %H:%M"),
            self.home_team,
            self.opposing_team, 
            f"{self.home_goals} : {self.opposing_goals}"
            )



@dataclass
class CompetitionTableSpot:
    """Represents a spot in current cometition's table."""
    team: str

    victories: int
    draws: int
    defeats: int

    @property
    def points(self) -> int:
        return self.victories * 2 + self.draws

    @classmethod
    def get_columns(cls) -> List[dict]:
        """Returns list of dictionarys with attributes that define how the column-headers should be displayed."""
        return [
            dict(header="Team", justify="left", style="cyan"),
            dict(header="Victories", justify="center", style="green"),
            dict(header="Draws", justify="center", style="yellow"),
            dict(header="Defeats", justify="center", style="red"),
            dict(header="Points", justify="center", style="blue"),
        ]

    def output_table_row(self) -> Tuple[str]:
        """Returns tuple of attributes of this instance. Number of items within tuple need to match the number of items from get_columns()."""
        return (
            self.team, 
            str(self.victories),
            str(self.draws),
            str(self.defeats),
            str(self.points),
        )

    def __lt__(self, other):
        if not isinstance(self, CompetitionTableSpot):
            raise ValueError(f"Got wrong input type for __lt__: {type(other)}")
        return self.points > other.points
    
    def __gt__(self, other):
        if not isinstance(self, CompetitionTableSpot):
            raise ValueError(f"Got wrong input type for __lt__: {type(other)}")
        return self.points < other.points
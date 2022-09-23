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
        pass

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

    def output_table_row(self) -> Tuple[str]:
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

    def output_table_row(self) -> Tuple[str]:
        return (
            self.team, 
            str(self.victories),
            str(self.draws),
            str(self.defeats),
            str(self.points)
        )

    def __lt__(self, other):
        if not isinstance(self, CompetitionTableSpot):
            raise ValueError(f"Got wrong input type for __lt__: {type(other)}")
        return self.points > other.points
    
    def __gt__(self, other):
        if not isinstance(self, CompetitionTableSpot):
            raise ValueError(f"Got wrong input type for __lt__: {type(other)}")
        return self.points < other.points
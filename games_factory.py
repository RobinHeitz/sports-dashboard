from typing import List, Tuple
from random import sample, randint
from datetime import datetime

from definitions import CompetitionTableSpot, DashboardItem, DashboardType, GameItem, GameResult, SportsType

HANDBALL_TEAMS = [
    "Füchse Berlin", "TWH Kiel", "SC Magdeburg", "Vfl Gummersbach", "ASV Hamm-Westfalen", "HSV Hamburg", "SG Flensburg-Handewit", "TV Lemgo", "Göppingen", "Melsungen"
]


def generate_dashboard_items() -> List[DashboardItem]:
    """Generates a list of dashboard items."""
    dashboard_items = list()

    dashboard_items.append(handball_bl_gameday_item())
    dashboard_items.append(handball_bl_placement_table_item())
    return dashboard_items


    
def handball_bl_gameday_item() -> DashboardItem:
    def _handball_bl_games() -> List[GameResult]:
        games = list()
        for i in range(5):
            home, opposing, *args = sample(HANDBALL_TEAMS, k=2, )

            game = GameResult(
                date=datetime.now(),
                home_team=home, 
                opposing_team=opposing,
                home_goals=randint(15,35),
                opposing_goals=randint(15,35),
            )
            games.append(game)
        return games

    games = _handball_bl_games()
    item = DashboardItem(
        title = "Handball Bundesliga, 1. Spieltag", 
        dashboard_type = DashboardType.gameday,
        game_items = games,
        sports_type=SportsType.handball
        )
    
    return item


def handball_bl_placement_table_item() -> DashboardItem:
    spots = []

    for team in HANDBALL_TEAMS:
        victories = randint(0,15)
        draws = randint(0,5)
        defeats = randint(2,10)
        spot = CompetitionTableSpot(team = team, victories=victories, draws=draws, defeats=defeats)
        spots.append(spot)
    
    spots = sorted(spots)

    item = DashboardItem(
        title = "Handball Bundesliga Tabelle 20. Spieltag", 
        sports_type=SportsType.handball, 
        dashboard_type=DashboardType.placement_table, 
        game_items=spots
    )
    return item

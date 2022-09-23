from unittest import TestCase
from definitions import CompetitionTableSpot, DashboardItem, DashboardType, GameItem, GameResult, SportsType
from games_factory import handball_bl_gameday_item, handball_bl_placement_table_item

from table_creation import _create_table, create_tables

from datetime import datetime

class TestGamesFactory(TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_dashboard_item(self) -> None:
        title = "Test Title"
        type = DashboardType.gameday
        games = [
            GameResult(datetime.now(), "Vfl Gummersbach", "ASV Hamm-Westfalen", 15, 20,),
            GameResult(datetime.now(), "SC Magdeburg", "Füchse Berlin", 35, 34,),
        ]
        sports_type = SportsType.handball


        item = DashboardItem(title=title, dashboard_type=type, game_items=games, sports_type=sports_type)
        self.assertIsNotNone(item)
        self.assertEqual(item.title, title)
        self.assertEqual(item.dashboard_type, type)
        self.assertEqual(len(item.game_items), len(games))
        for g in games:
            self.assertTrue(g in item.game_items)


    
    def test_bl_creation(self) -> None:
        item = handball_bl_gameday_item()
        self.assertIsNotNone(item.title)
        self.assertIsNot(len(item.game_items), 0)
        self.assertEqual(item.dashboard_type, DashboardType.gameday)
    
    
    def test_bl_competition_table_creation(self) -> None:
        item = handball_bl_placement_table_item()
        self.assertIsNotNone(item.title)
        self.assertIsNot(len(item.game_items), 0)
        self.assertEqual(item.dashboard_type, DashboardType.placement_table)

    def test_gameitemrender_method(self) -> None:
        game = GameResult(datetime.now(), "HomeTeam", "opposing Team", 33,33)
        render = game.output_table_row()
        self.assertEqual(
            len(render), 4
        )

class TestTableCreation(TestCase):

    def test_create_table(self):
        ...
        titel = "Test Title"
        games = [
            CompetitionTableSpot(team="Vfl Gummersbach", victories=1, draws=2, defeats=3),
            CompetitionTableSpot(team="THW Kiel", victories=3, draws=1, defeats=0),
            CompetitionTableSpot(team="SG Flensburg-Handewitt", victories=3, draws=1, defeats=0),
            CompetitionTableSpot(team="SC Magdeburg", victories=5, draws=1, defeats=0),
        ]

        item = DashboardItem(title=titel, sports_type=SportsType.handball, dashboard_type=DashboardType.placement_table, game_items=games)
        try:
            table = _create_table(item)
        except Exception:
            self.fail("Exception raised!")



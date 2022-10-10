from unittest import TestCase
from datetime import datetime

from handball.handball import list_bl_standings
from handball.definitions_hb import HandballPosition, HandballStandings


class TestHandballStandings(TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_create_handball_position(self) -> None:

        attrs = dict(
            position = 1, 
            team = "Rhein-Neckar-Löwen",
            played_games = "7/34",
            won = 7,
            draw = 0,
            lost = 0,
            points = "14:0",
            goal_difference = 50,
            goals_for = 255,
            goals_against = 205

        )
        try:

            HandballPosition(**attrs)

        except Exception as e:
            self.fail(f"Exception was thrown: {e}")
        


class TestHandballHTMLCodeParsing(TestCase):

    def test_html_code_offline(self) -> None:
        standings = list_bl_standings(testing = True)
        self.assertTrue(type(standings), HandballStandings)

    
    def test_html_code_offline(self) -> None:
        standings = list_bl_standings(testing = False)
        self.assertTrue(type(standings), HandballStandings)
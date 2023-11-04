from handball.definitions import Match, HandballTeamsChampionsLeague, ScheduledGameday
import datetime

from typing import Tuple, List

def process_scheduled_matches_cl(scheduled_games) -> List[Tuple[datetime.date, Match]]:

    matches = []
    
    for match in scheduled_games:

        divs = match.find_all("div")
        try:

            date_tags = divs[0].findChild("div").findChildren("span")
            date_str = date_tags[0].text.strip()
            date = datetime.datetime.strptime(date_str, "%a %b %d, %Y").date()
            
            time_str = date_tags[1].text.strip().split(",")[0]
            time = datetime.datetime.strptime(time_str, "%H:%M (%Z)").time()

        except:
            # continue if time cannot be parsed, meaning the match is not scheduled yet.
            continue

        home_team_spans = divs[2].findChildren("span")
        home_team = home_team_spans[0].text.strip()
        home_goals = home_team_spans[1].text
        
        away_team_spans = divs[3].findChildren("span")
        away_team = away_team_spans[0].text.strip()
        away_goals = away_team_spans[1].text

        try:
            assert home_team in HandballTeamsChampionsLeague
            assert away_team in HandballTeamsChampionsLeague

        except:
            continue


        if home_goals == 0 or away_goals == 0:
            match = Match(start_time=time, home_team=home_team, away_team=away_team)
        else:
            match = Match(start_time=time, home_team=home_team, away_team=away_team, already_played=True, home_goals=home_goals, away_goals=away_goals)

        matches.append(
            (date, match)
        )

    return matches        


def process_scheduled_gamedays_cl(matches: List[Tuple[datetime.date, Match]]):
    
    date_match_dict = {}

    for date, match in matches:

        if date not in date_match_dict:
            date_match_dict[date] = []
        if match not in date_match_dict[date]:
            date_match_dict[date].append(match)

    gamedays = [ScheduledGameday(date=date, matches=matches_list) for date, matches_list in date_match_dict.items()]
    return gamedays
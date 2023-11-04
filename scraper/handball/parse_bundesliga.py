import datetime
import re
from handball.definitions import ScheduledGameday, Match, HandballTeamsBundesliga


def process_scheduled_gamedays(scheduled_gamedays) -> dict:
    data = {}
    
    for schedule in scheduled_gamedays:
        # print(schedule)
        table = schedule.findChild("table")
        schedule_head = table.findChild("thead").findChild("tr")

        table_body = table.findChild("tbody")
        table_rows = table_body.findChildren("tr")

        data[schedule_head] = table_rows
    return data


def parse_date_of_matches(parsed_matched:dict):
    
    scheduled_gamedays_list = []

    
    for table_head, matches in parsed_matched.items():
        date_str = re.findall("(\d{1,2}\.\d{1,2}\.)", str(table_head))[0]

        cur_year = datetime.datetime.now().year

        date = datetime.datetime.strptime(date_str, "%d.%m.").date()
        if 1 <= date.month <= 7:
            date = date.replace(year=cur_year + 1)
        else:
            date = date.replace(year=cur_year)

        scheduled_gamedays_list.append(
            ScheduledGameday(date=date, matches=matches)
        )

    return scheduled_gamedays_list


def parse_paired_matches(schedules:dict):
    
    matches_dict = {}

    for schedule_headline, matches in schedules.items():
        matches_list = []

        for match in matches:

            # Time Parsing
            columns = match.findChildren("td")
            time_col = columns[0]
            try:
                time_str = str(time_col).split("\n")[1].strip()
                match_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            except:
                continue

            # Home and away team
            team_home_col = columns[1]
            team_home = team_home_col.findChild("a")
            team_home = str(team_home).split("\n")[3].strip()
      
            team_away_col = columns[3]
            team_away = team_away_col.findChild("a")
            team_away = str(team_away).split("\n")[3].strip()

            try:
                assert team_home in HandballTeamsBundesliga
                assert team_away in HandballTeamsBundesliga
            
            except:
                continue


            # goals
            result_col = columns[5]
            result = result_col.findChild("a")
            if result is None:
                game_pairing = Match(start_time=match_time, home_team=team_home, away_team=team_away)
            
            else:
                result = str(result).split("\n")[1].split(":")
                home_goals = result[0]
                away_goals = result[1]
                game_pairing = Match(
                    start_time=match_time,
                    home_team=team_home,
                    away_team=team_away,
                    already_played=True,
                    home_goals=home_goals,
                    away_goals=away_goals,
                    )

            matches_list.append(game_pairing)
        
        if len(matches_list) > 0:
            matches_dict[schedule_headline] = matches_list
    return matches_dict
    
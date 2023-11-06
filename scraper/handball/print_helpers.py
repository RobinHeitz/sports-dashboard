from .definitions import ScheduledGameday, MatchStats
from datetime import datetime

def print_gamedays(gamedays: list[ScheduledGameday]):
    for gameday in gamedays:
        print(f"====== New gameday on {gameday.date} with {len(gameday.matches)} matches:")
        for index, match in enumerate(gameday.matches):
            if match.already_played:
                print(f"={index +1}: {match.home_team} - {match.home_goals} vs {match.away_goals} - {match.away_team}")
            else:
                print(f"={index +1}: {match.home_team} vs {match.away_team}")
    print("---"*5)


def print_current_table(stats: list[MatchStats]):
    print("=== Starting table here:")
    for index, stat in enumerate(stats):
        print(f"= {index + 1}: {stat.team_name} {stat.matches_won}W {stat.matches_lost}L")
    print("---"*10)


def print_upcoming_matches(gamedays: list[ScheduledGameday]):
    gamedays_ = list(filter(lambda item: item.date > datetime.now().date(), gamedays))
    gamedays_ = sorted(gamedays_, key = lambda item: item.date, )
    print("===== Upcoming gamedays")
    for gameday in gamedays_[:3]:
        print(f"=== On {gameday.date}")
        for match in gameday.matches:
            print(f"{match.start_time}: {match.home_team} vs {match.away_team}")
    print("---"*5)



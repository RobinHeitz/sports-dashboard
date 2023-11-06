import yaml
from .definitions import MatchStats, ScheduledGameday

def calc_ranking(match_stats_list: list[MatchStats]):
    teams_sorted = sorted(
        match_stats_list, 
        key=lambda stats: (stats.points, stats.goal_ratio), 
        reverse=True)
    
    return teams_sorted


def calc_cur_table(gamedays_list: list[ScheduledGameday]):
    stats_dict = {}
    for gd in gamedays_list:
        for match in gd.matches:

            if not match.already_played:
                continue

            if match.home_team not in stats_dict:
                stats_dict[match.home_team] = MatchStats(team_name = match.home_team)

            if match.away_team not in stats_dict:
                stats_dict[match.away_team] = MatchStats(team_name = match.away_team)

            stats_dict[match.home_team].inc_games_played()
            stats_dict[match.away_team].inc_games_played()

            stats_dict[match.home_team].add_goals_scored(match.home_goals)
            stats_dict[match.home_team].add_goals_conceded(match.away_goals)

            stats_dict[match.away_team].add_goals_scored(match.away_goals)
            stats_dict[match.away_team].add_goals_conceded(match.home_goals)


            if match.home_team_won():
                stats_dict[match.home_team].inc_wins()
                stats_dict[match.away_team].inc_losses()

            elif match.away_team_won():
                stats_dict[match.home_team].inc_losses()
                stats_dict[match.away_team].inc_wins()
 
            elif match.draw_game():
                stats_dict[match.home_team].inc_draws()
                stats_dict[match.away_team].inc_draws()

            else:
                print('This error should not occuour')
                
    return calc_ranking(stats_dict.values())



if __name__ == "__main__":
    print('Hi there')

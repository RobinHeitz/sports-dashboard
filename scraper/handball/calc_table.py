import yaml

class MatchStats:
    team_name: str = ''
    matches_won: int = 0
    matches_lost: int = 0
    matches_drawn: int = 0
    games_played: int = 0
    goals_scored: int = 0
    goals_conceded: int = 0

    def __init__(self, team_name):
        self.team_name = team_name

    def __str__(self):
        return f'{self.team_name} {self.matches_won=} {self.matches_lost=}'

    def __repr__(self):
        return f'{self.team_name} {self.matches_won=} {self.matches_lost=}'


    def inc_games_played(self):
        self.games_played += 1

    def inc_wins(self):
        self.matches_won += 1

    def inc_losses(self):
        self.matches_lost += 1

    def inc_draws(self):
        self.matches_drawn += 1

    def add_goals_scored(self, goals):
        self.goals_scored += goals

    def add_goals_conceded(self, goals):
        self.goals_conceded += goals


def calc_ranking(match_stats_list):

    print('hi, Im calculating.')
    teams_sorted = sorted(
        match_stats_list, 
        key=lambda stats: stats.matches_won, 
        reverse=True)
    
    return teams_sorted


def calc_cur_table(gamedays_list):
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

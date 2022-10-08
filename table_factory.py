from data_management.definitions import FootballPosition, FootballStanding, FootballStageEnum, FootballTypeEnum
from data_management import football as fb

from rich.table import Table
from typing import Callable, List

def get_all_tables():

    return [
        # *create_football_cl_standings(),
        *create_football_bl_standings()

    ]

def create_football_cl_standings() -> List[Table]:
    def title(standing: FootballStanding):
        return f"Champions League: {standing.group}"
    
    title = f"Champions League"
    standings = fb.get_cl_standings(testing = True)
    standings = list(filter(lambda s: s.type == FootballTypeEnum.TOTAL, standings))
    return _create_football_standings(title, standings)

def create_football_bl_standings() -> List[Table]:
    def title(standing: FootballStanding):
        return f"Bundesliga"
    standings = fb.get_bl_standings(testing = True)
    standings = list(filter(lambda s: s.type == FootballTypeEnum.TOTAL, standings))
    return _create_football_standings(title, standings)



def _create_football_standings(table_title:Callable, standings:List[FootballStanding]) -> List[Table]:
    tables: List[Table] = list()
    
    for standing in standings:
        table = Table(title = table_title(standing))
        
        for c in FootballPosition.get_table_columns():
            table.add_column(c)

        for team in standing.table:
            table.add_row(*team.get_rows())

        tables.append(table)
    return tables
    




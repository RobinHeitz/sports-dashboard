from typing import List
from rich.table import Table

from .games_factory import generate_dashboard_items
from .definitions import DashboardItem, DashboardType, GameItem



def _create_table(item: DashboardItem) -> Table:
    """Returns a rich.table.Table - Object based on input DashboardItem."""
    table = Table(title=item.title)
    columns = item.game_items[0].get_columns()
    
    for column in columns:
        table.add_column(**column)
    
    for game in item.game_items:
        table.add_row(*game.output_table_row())
    
    return table

    
def create_tables() -> List[Table]:
    dashboard_items: List[DashboardItem] = generate_dashboard_items()
    return [_create_table(item) for item in dashboard_items]



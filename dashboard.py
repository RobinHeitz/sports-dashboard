from games_factory import generate_dashboard_items
from definitions import GameItem, DashboardItem, DashboardType


from typing import List, Callable, Tuple
from random import choices, randint, random

import typer
from rich.table import Table
from rich.console import Console


app = typer.Typer()
console = Console()

def _render_gameday(item:DashboardItem):
    """Renders a Table for a gamedays."""
    table = Table(title=item.title)
    table.add_column("Date", justify="center", style="green")
    table.add_column("Home team", style="blue")
    table.add_column("Opposing team", style="magenta")
    table.add_column("Result", justify="center",  style="red")

    for game in item.game_items:
        table.add_row(*game.output_table_row())
    console.print(table)



def _render_placement_table(item:DashboardItem):
    """Renders a Table for a competition tables."""
    table = Table(title = item.title)
    table.add_column("Team", style="cyan")
    table.add_column("Victories", style="blue", justify="center")
    table.add_column("Draws", style="magenta", justify="center")
    table.add_column("Defeats", style="red", justify="center")
    table.add_column("Points", style="blue", justify="center")

    for game in item.game_items:
        table.add_row(*game.output_table_row())
    console.print(table)


render_func_map = {
    DashboardType.gameday: _render_gameday, 
    DashboardType.placement_table: _render_placement_table, 
}

def render_dashboard_items(items: List[DashboardItem]) -> None:
    """Renders Table elements based on given DashboardItems."""
    for i in items:
        try:
            render_func = render_func_map[i.dashboard_type]
        except KeyError:
            raise NotImplementedError(f"The dashboard type {i.dashboard_type} is not implemented!")
        
        render_func(i)




@app.command()
def hello():

    dashboard_items: List[DashboardItem] = generate_dashboard_items()
    render_dashboard_items(dashboard_items)

    


if __name__ == "__main__":
    app()
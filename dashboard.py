from data_management.games_factory import generate_dashboard_items
from data_management.definitions import GameItem, DashboardItem, DashboardType

from data_management.table_creation import create_tables


from typing import List, Callable, Tuple
from random import choices, randint, random

import typer
from rich.table import Table
from rich.console import Console


app = typer.Typer()
console = Console()


@app.command()
def hello():
    
    tables = create_tables()
    for t in tables:
        console.print(t)



if __name__ == "__main__":
    app()
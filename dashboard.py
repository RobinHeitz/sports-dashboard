from typing import List, Callable, Tuple
from random import choices, randint, random

import typer
from rich.table import Table
from rich.console import Console

from table_factory import get_all_tables


app = typer.Typer()
console = Console()


@app.command()
def hello():
    
    tables = get_all_tables()
    for t in tables:
        console.print(t)


if __name__ == "__main__":
    app()
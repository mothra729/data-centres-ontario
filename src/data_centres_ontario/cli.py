"""Console script for data_centres_ontario."""

import typer
from rich.console import Console

from data_centres_ontario import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for data_centres_ontario."""
    console.print("Replace this message by putting your code into data_centres_ontario.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()

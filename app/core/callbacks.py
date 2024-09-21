import typer
from rich import print
from app import __version__

# Version callback   
def version_callback(present: bool):
    if present:
        print(__version__)
        raise typer.Exit()
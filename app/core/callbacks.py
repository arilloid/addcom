import typer
from rich import print
from app import __version__

 
def version_callback(provided: bool):
    """
    Print current tool version if a flag option was provided
    """
    if provided:
        print(__version__)
        raise typer.Exit()
import typer
from rich import print
from app import __version__
from app.core.file_operations import load_contents

 
def version_callback(provided: bool):
    """
    Print current tool version if a flag option was provided
    """
    if provided:
        print(__version__)
        raise typer.Exit()
    

def context_callback(context_file: str) -> str:
    """
    Load contents of example file
    """
    if context_file:
        context_contents = load_contents(context_file)
        return context_contents

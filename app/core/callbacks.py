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
    

def context_callback(context_files: list[str]) -> list[str]:
    """
    Load contents of example files
    """
    context_contents = [load_contents(file) for file in context_files]
    
    return context_contents
  
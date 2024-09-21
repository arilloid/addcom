import typer
from rich import print
from typing_extensions import Annotated
from typing import Optional

from app.core.callbacks import version_callback
from app.core.file_operations import load_contents
from app.core.api import generate_comments

# Create Typer instance
app = typer.Typer(no_args_is_help=True)

@app.command()
def add_comments( 
    files: Annotated[
        Optional[list[str]],
        typer.Argument(..., help="The Source Code files"),
    ],
    version: Annotated[Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Get the version number",
            is_eager=True,
            callback=version_callback,
        ),
    ] = None,
):
    """
    Add comments to each of the provided files.
    """
    for file in files:
        content = load_contents(file)
        if content:
            comments = generate_comments(content)
            print(f"--- {file} with added comments ---")
            print(comments)


if __name__ == '__main__':
    app()

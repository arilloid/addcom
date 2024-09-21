import typer
from rich import print
from typing_extensions import Annotated
from typing import Optional
from app.core.callbacks import version_callback
from app.core.file_operations import load_contents
from app.core.api import generate_comments

# Create Typer instance
app = typer.Typer()


@app.command()
def add_comments(
    file_paths: Annotated[
        list[str],
        typer.Argument(..., help="Paths to source code files to be commented"),
    ],
    version: Annotated[Optional[bool],
        typer.Option( "--version", "-v",
            help="See the current tool version",
            is_eager=True,
            callback=version_callback,
        ),
    ] = None,
):
    """
    Add comments to each of the provided files.
    """
    for file_path in file_paths:
        content = load_contents(file_path)
        if content:
            commented_content = generate_comments(content)
            print(f"--- {file_path} with added comments ---")
            print(commented_content)
            print()


if __name__ == '__main__':
    app()

import typer
from rich import print
from typing_extensions import Annotated
from typing import Optional
from app.core.callbacks import version_callback
from app.core.file_operations import load_contents, write_to_output_file
from app.core.api import generate_comments

# Create Typer instance
app = typer.Typer()


@app.command()
def add_comments(
    file_paths: Annotated[
        list[str],
        typer.Argument(..., 
            help="Paths to source code files to be commented"
        )
    ],
    version: Annotated[Optional[bool],
        typer.Option( "--version", "-v",
            help="See the current tool version",
            is_eager=True,
            callback=version_callback,
        )
    ] = None,
    output: Annotated[Optional[str],
        typer.Option("--output", "-o", 
            help="Specify an output filename to save the commented code"
        )
    ] = None,
    api_key: Annotated[Optional[str],
        typer.Option("--api-key", "-a", 
            help="Provide API key for authentication"
        )
    ] = None,
    base_url: Annotated[Optional[str],
        typer.Option("--base-url", "-u", 
            help="Specify base URL for the API"
        )
    ] = None,
    model: Annotated[Optional[str],
        typer.Option("--model", "-m", 
            help="Specify a LLM to use for comment generation"
        )
    ] = None,
    stream: Annotated[Optional[bool],
        typer.Option("--stream", "-s", 
            help="Stream the response live as it updates"
        )
    ] = False,
):
    """
    Add comments to each of the provided files.
    """
    for file_path in file_paths:
        content = load_contents(file_path)

        commented_content = generate_comments(file_path, content, api_key, base_url, model, stream)

        if output:
            write_to_output_file(output, commented_content)
        elif not stream:
            print(f"--- {file_path} with added comments ---\n\n")
            print(commented_content + "\n\n")


if __name__ == '__main__':
    app()

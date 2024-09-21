from groq import Groq
import typer
from rich import print
import os
import sys
from typing_extensions import Annotated
from typing import Optional
from app import __version__


# Create Typer instance
app = typer.Typer(no_args_is_help=True)

# Initialize Groq client
client = Groq(
    api_key=os.getenv('GROQ_API_KEY')
)

# Create system prompt
prompt = (
    "You are a coding assistant. When provided with the contents of a code file, your task is to add appropriate "
    "comments to explain it's functionality where necessary. Comments should be formatted according to best practices. "
    "Return modified code with the added comments and no additional text or explanation as plain text"
)


def load_contents(filepath):
    """
    Read the contents of a file and return it. If the file is not found,
    print an error message and return None.
    """
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}", file=sys.stderr)
        return None

    with open(filepath, 'r') as file:
        return file.read()


def generate_comments(content: str):
    """
    Send the file content to the Groq API to generate comments.
    Returns the code with generated comments.
    """
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-8b-8192",
    )
    comments_content = response.choices[0].message.content
    token_usage = response.usage
    return comments_content, token_usage



# Version callback   
def version_callback(present: bool):
    if present:
        print(__version__)
        raise typer.Exit()



# Version callback   
def version_callback(present: bool):
    if present:
        print(__version__)
        raise typer.Exit()

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
    ] = None, token_usage: bool = typer.Option(False, "--token-usage", "-t", help="Get the number of tokens used in the request")
):
    """
    Add comments to each of the provided files.
    """
    for file in files:
        content = load_contents(file)
        if content:
            comments, token_usage_data = generate_comments(content)
            print(f"--- {file} with added comments ---")
            print(comments)
            print()
    if token_usage:
        print(f"--- Token usage for {file} ---")
        print("Completion_tokens: ", token_usage_data.completion_tokens)
        print("Prompt_tokens: ", token_usage_data.prompt_tokens)
        print("Total_tokens: ", token_usage_data.total_tokens)
        print()


if __name__ == '__main__':
    app()

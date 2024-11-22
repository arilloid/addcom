# Thanks for taking the time to contribute ❤️

If you spot bugs or have any enhancement suggestions for the project, don't hesitate to create an Issue and open a Pull Request! 

## Prerequisites 

> `addcom` uses [Poetry](https://python-poetry.org/) for dependency management and packaging. Ensure that Poetry is installed on your system before getting started!

To install Poetry, run the following command:

```sh
pip install poetry
```

## Project Setup 

#### 1. Fork the repository and clone it to your local machine.

#### 2. After cloning the repo cd into the project folder and simply run:
   
```sh
poetry install
```

This command will automatically create a virtual environment & install all the necessary dependencies + the project package itself within it, making it ready for development.

#### 3. Run the tool:

```sh
poetry run addcom
```

Refer to the setup instructions in [README.md](https://github.com/arilloid/addcom/blob/main/README.md#setup-instructions) for more details.

## Testing 

This project uses `pytest` for unit testing and `pytest-mock` for mocking.

You can execute all unit tests by running:

```sh
poetry run pytest
```

## Code Formatting & Linting

Addcom uses [Black](https://pypi.org/project/black/) for code formatting and [Ruff](https://docs.astral.sh/ruff/) for linting. 

### IDE Integration

**VSCode**: The repository includes a pre-configured `settings.json` file located in the `.vscode` directory. This configuration enables automatic formatting and linting on save.

To take full advantage of automatic formatting and linting, please install the following Visual Studio Code extensions:
- [Black VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

> If you are using a different IDE, please refer to the integration documentation for both tools to set up linting and formatting: [Black IDE Integration](https://black.readthedocs.io/en/stable/integrations/editors.html), [Ruff IDE Integration](https://docs.astral.sh/ruff/editors/)
> 
> OR perform formatting and linting mannualy following the instructions below.

### Manual Formatting & Linting

#### Format your code

Format the files you modified mannualy by running:

```sh
poetry run black {source_file_or_directory}
```

Format the entire project by running Black from the root of the repo:

```sh
poetry run black .
```

#### Lint your code

You can lint the files manually by running: 

```sh
poetry run ruff check --fix {source_file_or_directory}
``` 

You can also run Ruff from the root of the repo to lint the entire project:

```sh
poetry run ruff check --fix .
```

# Thanks for taking the time to contribute ❤️

If you spot bugs or have any enhancement suggestions for the project, don't hesitate to create an Issue and open a Pull Request! 

## Project Setup 

Right now, since the tool is not distributed through any package managers, the setup instructions for both users and developers are practically identical.
Fork the repo and follow the setup instructions in [README.md]([https://github.com/arilloid/addcom/blob/main/README.md#](https://github.com/arilloid/addcom/blob/main/README.md#setup-instructions)).

## Testing 

To test your code changes, you can manually rebuild the tool by rerunning the following command in the root of the project:

```sh
pip install .
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

Install both of the tools using `pip`:

```sh
pip install black
pip install ruff
```

#### Format your code

Format the files you modified mannualy by running:

```sh
black {source_file_or_directory}
```

Format the entire project by running the python script located at the root of the repo:

```sh
python format.py
```

#### Lint your code

You can lint the files manually by running: 

```sh
ruff check --fix {source_file_or_directory}
``` 

You can also run the script located at the root of the repo to lint the entire project

```sh
python lint.py
```

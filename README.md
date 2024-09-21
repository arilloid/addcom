# ADDCOM

`addcom` is a CLI source code documenter tool which provides coders with an easy way to add comments to their source code files.
Give it a relative/absolute path to your file and it will analyze its contents and add comments using Meta's LLM.

![addcom](https://github.com/user-attachments/assets/e01f1c1b-faf4-4c2d-b62b-a2492de1475b)

# Setup Instructions

#### 1. After cloning the repo cd into the project folder and simply run:

```cmd
pip install .
```

#### 2. Create an account and generate the API key here -> https://console.groq.com/

#### 3. Expose the API key to the terminal

Command Prompt

```cmd
set GROQ_API_KEY=your_api_key_here
```

Poweshell

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

Bash

```bash
$env:GROQ_API_KEY="your_api_key_here"
```

#### 4. Run addcom

```cmd
 addcom [FILEPATH]
```

## Options

- `--token--usage, -t`: Get the number of tokens used in the request
- `-h, --help`: Display help for command

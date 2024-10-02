# ADDCOM

`addcom` is a CLI source code documenter tool which provides coders with an easy way to add comments to their source code files. 
Give it a relative/absolute path to your file and it will analyze its contents and add comments using a Large Language Model's chat completion. 

![addcom](https://github.com/user-attachments/assets/e01f1c1b-faf4-4c2d-b62b-a2492de1475b)

See a demo of the functionality on YouTube: [addcom-demo](https://youtu.be/3jKifG2BLzc?si=M2MNCW2BASBnDQ7z)

# Setup Instructions

### Prerequisites 

> Make sure Python is installed on your system (you can download it here: https://www.python.org/downloads/).

#### 1. After cloning the repo cd into the project folder and simply run:
   
```cmd
pip install .
```

#### 2. Default: Create an account and generate the API key here: https://console.groq.com/
By default, addcom uses the Groq API endpoint for chat completion. However, you can specify a custom endpoint using the `--base-url` or `-u` flag option. (If you do this, make sure to obtain an appropriate API key and specify the model supported by the chosen provider using the `--model`/ `-m` option).

#### 3. Set the API key

To do this you can expose the API key to the terminal:

  Command Prompt
  
   ```cmd
   set GROQ_API_KEY=your_api_key_here
   ```
  
  PowerShell
  
  ```powershell
  $env:ADDCOM_API_KEY="your_api_key_here"
  ```
  
  Bash
  
  ```bash
  $env:ADDCOM_API_KEY="your_api_key_here"
  ```

or provide the key using the `--api-key`/ `a` flag.

#### 4. Run addcom.
   
```cmd
 addcom [OPTIONS] FILE_PATH(S)...
```

# Usage 

### Arguments

You can add comments to one or multiple source code files. Just type addcom and specify the file paths. 

```cmd
 addcom examples/sample.py examples/test.py
```

### Options

| Option          | Shortcut | Type   |                                                       | Default |
| --------------- | -------- | ------ | ----------------------------------------------------- | ------- |
| `--help`        |          | FLAG   | Show help message                                     | `N/A`   |
| `--version`     | `-v`     | FLAG   | See the current tool version                          | `N/A`   |
| `--context`     | `-c`     | PATH   | Path to example file to provide context for the LLM   | None    |
| `--output`      | `-o`     | PATH   | Specify an ouput filename to save the commented code  | None    |
| `--stream`      | `-s`     | FLAG   | Stream the response live as it updates                | None    |
| `--api-key`     | `-a`     | TEXT   | Provide API key for authentication                    | None    |
| `--base-url`    | `-u`     | TEXT   | Specify base URL for the API                          | None    |
| `--model `      | `-o`     | TEXT   | Specify a LLM to use for comment generation           | None    |


## Configuration via TOML file

The functionality to provide arguments via a TOML file has been provided as well, you can find more information about a TOML file [here](https://toml.io/en/) 

if you want to pre-define the arguments for the CLI tool, you can add the arguments in the `addcom_config.toml` file as well in the home directory

this will only work if you have `addcom_config.toml` in the home directory
the supported arguments as of now are:


`model` - specifies the model of groq to be used
`stream` - can be set to "true" or "false"
`api_key` - specifies the api_key to be used for the API
`context` - specifies the context file to provide 

1. A sample configuration file `config.toml.example` is provided in the repository.
2. To create your own configuration file, run the following command:

   ```sh
   cp config.toml.example ~/addcom_config.toml
   ```

   

### Notes
`--output` / `-o` - If multiple files are specified, the commented source code from all files will be combined and saved into a single output file.

`--api-key` / `-a` - As mentioned above, there are 2 ways to provide the API key to the tool, passing the API key using this option will override the API key that was exposed to the terminal.

`--model`/ `-m` - You can find models compatible with the default API endpoint here: https://console.groq.com/docs/models


`--base-url` / `u` - If you decide to use a custom API endpoint, make sure to obtain an API key and specify a Large Language Model supported by the API of your choice.

`Windows Path Handling`: When specifying the location of the context file, using standard Windows path single backslashes (\) can cause parsing errors, as tomllib treats those as escape characters. Windows users should specify paths with double backslashes (e.g., context = "examples\\commented.py" instead of context = "examples\commented.py").

#### Example: using OpenRouter API as base URL

```cmd
 addcom -u https://openrouter.ai/api/v1 -a "your_api_key" -m meta-llama/llama-3.1-8b-instruct:free examples/test.py
```

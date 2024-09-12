# ADDCOM

`addcom` is a CLI source code documenter tool which provides coders with an easy way to add comments to their source code files. 
Give it a relative/absolute path to your file and it will analyze its contents and add comments using Meta's LLM. 


![addcom](https://github.com/user-attachments/assets/59479087-57fe-4d55-9bfb-1e48c0379023)

# Setup Instructions


1. After cloning the repo cd into the project folder and simply run:

  ```cmd
  pip install .
  ```

2. Since addcom was build using Groq API, you have to have a valid API key to use the tool.
   Create an account and generate the API key here -> https://console.groq.com/

3. Expose the API key
   - Command Prompt
     ```cmd
     set GROQ_API_KEY=your_api_key_here
     ```
   - Poweshell
     ```powershell
     $env:GROQ_API_KEY="your_api_key_here"
     ```
   - Bash
     ```bash
     $env:GROQ_API_KEY="your_api_key_here"
     ```

4. Run addcom
   ```cmd
     addcom samples/test.py
   ```
   


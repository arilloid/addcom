from openai import OpenAI
from rich import print
import sys
import os


# Create system prompt
prompt = (
    "You are a coding assistant. When provided with the contents of a code file, your task is to add appropriate "
    "comments to explain it's functionality where necessary. Comments should be formatted according to best practices. "
    "Return modified code with the added comments and no additional text or explanation as plain text"
    "Make sure to not wrap the code in any brackets."
)


def generate_comments(file_path: str, content: str, api_key: str, url: str, model: str, stream: bool) -> str:
    """
    Send the file content to the API endpoint to generate comments.
    Returns the code with generated comments.
    """
    # Use environment variable for API key if it was not provided
    api_key = api_key or os.getenv('ADDCOM_API_KEY')

    # Check if API key was successfully set
    if not api_key:
        print("Error: API key must be provided either as an argument or through the environment.", file=sys.stderr)
        sys.exit(1)

    # Use Groq API endpoint as default if base URL not provided
    base_url = url or "https://api.groq.com/openai/v1"

    # Use LLama3 model as default if model option not provided
    model = model or "llama3-8b-8192"

    # Initialize OpenAI client (default = Groq API endpoint)
    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    try:
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
            model=model,
            stream=stream
        )
        
        if not stream:
            return response.choices[0].message.content
        else:
            # Store streamed content
            streamed_content = ""

            print(f"--- {file_path} with added comments ---\n\n")

            # Print each chunk to stdout as it arrives and accumulate content
            for chunk in response:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content:
                    print(chunk_content, end='', flush=True)
                    streamed_content += chunk_content

            print("\n\n")
            
            # Return complete content for saving to file if necessary
            return streamed_content
    
    except Exception as e:  # You can specify a more specific exception here
        print(f"Error occurred while making an API call: {e}", file=sys.stderr)
        sys.exit(1)
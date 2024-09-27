from openai import OpenAI
import sys
import os

def build_prompt_messages(content: str, context: list[str]) -> list[dict]:
    """
    Constructs messages for the LLM
    """
    # Create system prompt
    system_prompt = (
        "You are a coding assistant. When provided with the contents of a code file, your task is to add appropriate "
        "comments to explain it's functionality where necessary. Comments should be formatted according to best practices."
        "You can be provided with example code to use as a reference for comment style. Each snippet will be prefixed"
        " with 'Example:'. Return modified code with the added comments and no additional text or explanation, as plain text"
        "Make sure to not wrap the code in any brackets."
    )

    # Initialize message list with the system prompt
    messages = [{"role": "system", "content": system_prompt}]

    # Add context files's contents as previous interactions - few-shot learning
    for context_file_content in context:
        messages.append({"role": "user", "content": f"Example:\n{context_file_content}"})
        messages.append({
            "role": "assistant", 
            "content": (
                "Great! Please provide another example if you have one, "
                "or share the source code file you'd like me to comment on."
            )
        })


def generate_comments(content: str, context: list[str], api_key: str, url: str, model: str) -> str:
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
        )
        
        return response.choices[0].message.content
    
    except Exception as e:  # You can specify a more specific exception here
        print(f"Error occurred while making an API call: {e}", file=sys.stderr)
        sys.exit(1)
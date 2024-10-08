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
            messages=build_prompt_messages(content, context),
            model=model,
        )
        
        return response.choices[0].message.content
    
    except Exception as e:  # You can specify a more specific exception here
        print(f"Error occurred while making an API call: {e}", file=sys.stderr)
        sys.exit(1)
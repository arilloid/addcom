from groq import Groq
import os

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

def generate_comments(content: str) -> str:
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
    return response.choices[0].message.content
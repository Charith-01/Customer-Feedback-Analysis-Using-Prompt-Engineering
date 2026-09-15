# Import required libraries
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_response(prompt):
    """Send a prompt to Gemini and return the generated text."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
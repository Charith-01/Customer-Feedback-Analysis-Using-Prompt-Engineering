import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError, ClientError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

client = genai.Client(api_key=api_key)


def generate_response(prompt, max_retries=5):
    """Send a prompt to Gemini with retry handling."""

    for attempt in range(max_retries):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except ServerError:
            wait_time = 10 * (attempt + 1)

            if attempt < max_retries - 1:
                print(
                    f"Gemini server busy. "
                    f"Retrying in {wait_time} seconds..."
                )
                time.sleep(wait_time)
            else:
                raise

        except ClientError as error:

            # Handle Gemini free-tier rate/quota errors
            if "429" in str(error) or "RESOURCE_EXHAUSTED" in str(error):

                wait_time = 60

                if attempt < max_retries - 1:
                    print(
                        f"Gemini rate limit reached. "
                        f"Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)
                else:
                    raise
            else:
                raise
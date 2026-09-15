# Import the reusable LLM function
from llm_client import generate_response

# Test Gemini connection
prompt = "Reply with exactly: Model connection successful"

response = generate_response(prompt)

print(response)
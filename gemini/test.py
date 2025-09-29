from google import genai
from google.genai import types
client = genai.Client(api_key="dfafafaffafdaf")

response = client.models.generate_content(
    model="gemini-2.5-pro", contents="please introduce yourself"
)
print(response.text)
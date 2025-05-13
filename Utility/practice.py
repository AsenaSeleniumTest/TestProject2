from google import genai
from google.genai.types import HttpOptions

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(model="gemini-2.0-flash-001",contents="How do I configure appium in python for mobile testing?",)

print(response.text)
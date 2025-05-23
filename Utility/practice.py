from google import genai
from google.genai.types import HttpOptions



client = genai.Client(http_options=HttpOptions(api_version="v1",api_key=API_KEY))
response = client.models.generate_content(model="gemini-2.0-flash-001",contents="How do I configure appium in python for mobile testing?",)

print(response.text)

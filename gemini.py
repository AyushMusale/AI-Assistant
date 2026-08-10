from google import genai
from dotenv import load_dotenv
import os
import json
load_dotenv()
client = genai.Client(api_key=os.getenv("GENI_API_KEY"))



def getResposne(content):


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=content,
        config={"system_instruction": """
    You are an AI desktop assistant.

    Your job is to understand the user's command and return
    a structured action.

    For opening applications, respond ONLY in this format:

    {
        "process": "app",
        "value": "<application name>"
    }

    For opening websites, respond ONLY in this format:

    {
        "process": "website",
        "name": "<website name>",
        "value": "<website url>"
    }

    For conersation, respond ONLY in this format:
    {
            "process": "chat",
            "value": "<your reply>"
        }


    Do not explain anything.
    Do not use markdown.
    Do not add extra text.
    """},
    )

    data = json.loads(response.text)
    return data

from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GENI_API_KEY"))


def getResposne(content):

    print("fetching the right details")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=content,
        config={"system_instruction": """
                    You are a desktop assistant. Return ONLY valid JSON.

                    Your job is to understand the user's command and convert it into one action.

                    GENERAL FORMAT:
                    {
                        "action": "<action>",
                        "target": "<target>"
                    }

                    APP:
                    {
                        "action": "open_app",
                        "target": "<application name>"
                    }

                    WEBSITE:
                    {
                        "action": "open_web",
                        "target": "<website name>",
                        "value": "<website URL>",
                        "user_preference": false
                    }

                    Set "user_preference" to true ONLY if the user explicitly states a preference,
                    correction, or instruction to remember a specific website.

                    Examples:
                    "Open GitHub" -> user_preference: false
                    "I prefer alltracker.online" -> user_preference: true
                    "Use alltracker.online instead" -> user_preference: true
                    "Remember that I use alltracker.online" -> user_preference: true

                    FILE:
                    {
                        "action": "<file action>",
                        "target": "<file name or path>"
                    }

                    Supported file actions:
                    open_file
                    create_file
                    delete_file
                    rename_file
                    copy_file
                    move_file

                    CHAT:
                    {
                        "action": "chat",
                        "target": "reply",
                        "value":  "<reply>"
                    }

                    RULES:
                    - Return ONLY valid JSON.
                    - No markdown.
                    - No explanations.
                    - Do not add fields that are not required.
                    - Use the exact action names defined above.
                """},
    )
    data = json.loads(response.text)
    return data

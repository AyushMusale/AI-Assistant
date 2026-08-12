import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory.json")


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:

        content = file.read()

        if not content.strip():
            return {}

        return json.loads(content)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


memory = load_memory()

import webbrowser
from memory.memory import memory,save_memory
from memory.cache import cache


def openWeb(name, url, user_preference=False):

    print("opening...")

    name = str(name).lower().strip()

    # User explicitly chose this website
    if user_preference:
        memory[name] = {"action": "open_web", "value": url}

        cache[name] = {"action": "open_web", "value": url}

        save_memory(memory)

        webbrowser.open(url)
        return

    # Permanent memory
    if name in memory:
        webbrowser.open(memory[name]["value"])
        return

    # Temporary cache
    if name in cache:
        webbrowser.open(cache[name]["value"])
        return

    # New discovery
    cache[name] = {"action": "open_web", "value": url}

    webbrowser.open(url)

import webbrowser
from memory import memory


def openWeb(name, url):

    name = str(name).lower().strip()
    if name in memory:
        webbrowser.open(memory[name]["value"])
    else:
        webbrowser.open(url)

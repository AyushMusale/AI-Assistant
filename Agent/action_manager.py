from tools.web.webmanager import openWeb
from tools.app.appmanager import openApp


def actionManager(data):
    action = data["action"]
    target = data["target"]

    if action == "open_app":
        openApp(target)
    if action == "open_web":
        value = data["value"]
        openWeb(target, value, user_preference=False)
    if action == "chat":
        value = data["value"]
        print(value)

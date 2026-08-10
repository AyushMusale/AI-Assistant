from webmanager import openWeb
from appmanager import openApp
from gemini import getResposne
from local_router import local_router
from memory import memory

if __name__ == "__main__":

    active = True

    while active:
        userInput = input("How can i help you: ")

        result = local_router(userInput, memory)
        if result:
            if result["memory"]["type"] == "app":
                openApp(result["target"])

            elif result["memory"]["type"] == "website":
                openWeb(result["target"], result["memory"]["value"])

        else:
            data = getResposne(userInput)

            if data["process"] == "website":
                openWeb(data["name"], data["value"])

            elif data["process"] == "app":
                openApp(data["value"])

            elif data["process"] == "chat":
                print(data["value"])

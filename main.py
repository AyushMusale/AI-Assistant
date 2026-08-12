from Agent.gemini import getResposne
from local_router import local_router
from memory.memory import memory
from memory.cache import cache

from Agent.action_manager import actionManager

if __name__ == "__main__":

    active = True

    while active:
        userInput = input("How can I help you: ")

        result = local_router(userInput, memory, cache) 
        print(result)
        if result is None:
            result = getResposne(userInput)

        actionManager(result)

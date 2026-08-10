from appmanager import find_app
from memory import memory, save_memory

ACTION_WORDS = {"open", "launch", "start", "run", "visit"}


def local_router(user_input, memory):

    text = user_input.lower().strip()
    words = text.split()

    # Explicit command
    if words and words[0] in ACTION_WORDS:

        target = " ".join(words[1:]).strip()
        # 1. Check memory
        if target in memory:

            return {"action": "open", "target": target, "memory": memory[target]}

        # 2. Not in memory -> search PC
        path = find_app(target)

        if path is not None:
            return {
                "action": "open",
                "target": target,
                "memory": {"type": "app", "value": path},
            }

    return None

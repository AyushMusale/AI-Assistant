ACTION_WORDS = {"open", "launch", "start", "run", "visit"}


def local_router(user_input, memory, cache):

    text = user_input.lower().strip()
    words = text.split()
    if words and words[0] in ACTION_WORDS:

        target = " ".join(words[1:]).strip()
        if target in memory:
            return {
                "action": memory[target]["action"],
                "target": target,
                "value": memory[target]["value"],
                "source": "memory",
            }
        if target in cache:
            return {
                "action": cache[target]["action"],
                "target": target,
                "value": cache[target]["value"],
                "source": "cache",
            }

    return None

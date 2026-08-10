import subprocess
import os
from memory import memory, save_memory, load_memory


def find_app(app_name):

    locations = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        os.path.expanduser(r"~\AppData\Local"),
        os.path.expanduser(r"~\AppData\Roaming"),
    ]

    target = app_name.lower() + ".exe"

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if file.lower() == target:

                    path = os.path.join(root, file)

                    memory[app_name.lower()] = {
                        "type": "app",
                        "value": path,
                    }
                    save_memory(memory)

                    return path

    return None


def openApp(name):

    name = name.lower().strip()
    if name in memory:
        path = memory[name]["value"]

        if os.path.exists(path):
            subprocess.Popen(
                path,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return

        # Remove stale memory
        del memory[name]
        save_memory(memory)

    path = find_app(name)

    if path is not None:
        subprocess.Popen(
            path,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return
    else:
        print("Not Found")

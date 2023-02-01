_just_started = False


def startup_once():
    global _just_started
    if _just_started:
        return

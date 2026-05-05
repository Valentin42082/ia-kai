BOT_NAME = "kai"

def detect_kai(content):

    content = content.lower()

    triggers = [
        "kai",
        "@kai",
        "hey kai",
        "salut kai",
        "bonjour kai"
    ]

    return any(
        trigger in content
        for trigger in triggers
    )

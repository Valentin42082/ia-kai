import json
import random

with open("ia/personality.json", "r", encoding="utf-8") as f:
    personality = json.load(f)

def get_response(mood, user):

    responses = personality["personalities"][mood]

    return random.choice(responses).format(
        user=user
    )

def get_welcome_message(user):

    return personality["welcome_message"].format(
        user=user
    )

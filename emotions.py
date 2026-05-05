# =========================================
# FICHIER : ia/emotions.py
# =========================================

from datetime import datetime
import random

def get_current_mood():

    hour = datetime.now().hour

    moods = []

    # Nuit
    if 1 <= hour <= 6:
        moods = [
            "tired",
            "serious"
        ]

    # Journée
    elif 7 <= hour <= 18:
        moods = [
            "happy",
            "friendly",
            "serious"
        ]

    # Soir
    else:
        moods = [
            "serious",
            "chaotic",
            "friendly"
        ]

    return random.choice(moods)

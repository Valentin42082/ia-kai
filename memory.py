user_memory = {}

def remember_user(user_id, username):

    user_memory[user_id] = {
        "name": username
    }

def get_user(user_id):

    return user_memory.get(user_id)

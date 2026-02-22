def get_user(user_id):
    if user_id > 0:
        return {"id": user_id, "name": "John"}
    return None

def save_user(user):
    if "name" not in user:
        raise ValueError("User must have a name")
    return True

def delete_user(user_id):
    if user_id > 0:
        print("Deleting")
        return True
    return False
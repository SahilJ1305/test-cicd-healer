def get_user(user_id):
    if user_id > 0:
    return {"id": user_id, "name": "John"}  # bad indent — INDENTATION bug, line 3
    return None

def save_user(user):
        name = user["name"]   # bad indent — INDENTATION bug, line 7
        return True

def delete_user(user_id):
    if user_id > 0:
            print("Deleting")  # bad indent — INDENTATION bug, line 12
            return True
    return False

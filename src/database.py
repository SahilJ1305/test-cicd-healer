def get_user_query(user_id):

    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query

def connect_db():
    return "Connected to Database"

def get_user(user_id):
    if user_id < 0:
        return None
    return {"id": user_id}

def save_user(user_data):
    return True

def delete_user(user_id):
    return True
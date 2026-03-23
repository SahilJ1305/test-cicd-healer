def get_user(user_id):

    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def save_user(user_data):

    return "User saved"

def delete_user(user_id):

    return "User deleted"

def connect_db():
    return "Connected to Database"
def get_user_query(user_id):
    # ERROR: TYPE_ERROR - Cannot concatenate string and integer
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def connect_db():
    return "Connected to Database"

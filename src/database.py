def get_user_query(user_id):
    
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def connect_db():
    return "Connected to Database"

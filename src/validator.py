def validate_input(data):
    if not data:
        return False
    return True

def is_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

def is_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    return False
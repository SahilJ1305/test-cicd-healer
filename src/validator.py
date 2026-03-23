def is_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

def is_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    return False

def validate_user_input(user_input):
    if len(user_input) == 0:
        print("Input cannot be empty!")
    else:
        print("Valid input received.")
    return True
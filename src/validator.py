def is_email(email)        
    if "@" in email:
        return True
    return False

def is_phone(number)       
    if len(number) == 10:
        return True
    return False

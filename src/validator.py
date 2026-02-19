def is_email(email)        # missing colon — SYNTAX bug, line 1
    if "@" in email:
        return True
    return False

def is_phone(number)       # missing colon — SYNTAX bug, line 6
    if len(number) == 10:
        return True
    return False

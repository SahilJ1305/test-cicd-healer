from src.validator import is_email, is_phone

def test_valid_email():
    assert is_email("test@gmail.com") == True

def test_invalid_email():
    assert is_email("notanemail") == False

def test_valid_phone():
    assert is_phone("1234567890") == True

def test_invalid_phone():
    assert is_phone("123") == False

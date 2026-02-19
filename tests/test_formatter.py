from src.formatter import format_greeting, format_price, repeat_word

def test_greeting():
    assert format_greeting("Alice", 25) == "Hello Alice you are 25 years old"

def test_price():
    assert format_price(9.99) == "$9.99"

def test_repeat():
    assert repeat_word("hello", 3) == "hellohellohello"

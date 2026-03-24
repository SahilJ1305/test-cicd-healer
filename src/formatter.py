def format_report(data):
    header = "--- REPORT ---"
    body = f"Data: {data}"
    return f"{header}\n{body}"

def format_greeting(name, age):
    return f"Hello {name} you are {age} years old"

def format_price(price):
    return f"${price:.2f}"

def repeat_word(word, times):
    return word * times
def format_greeting(name, age):
    return "Hello " + name + " you are " + age + " years old"  # int + str — TYPE_ERROR, line 2

def format_price(price):
    return "$" + price  # float + str — TYPE_ERROR, line 5

def repeat_word(word, times):
    return word * "3"   # str * str — TYPE_ERROR, line 8

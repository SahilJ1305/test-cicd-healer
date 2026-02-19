def multiply(a, b):
    return a + b       # wrong operator — LOGIC bug, line 2

def is_even(n):
    return n % 2 == 1  # wrong condition — LOGIC bug, line 5

def max_of_two(a, b):
    if a > b:
        return b       # returns wrong value — LOGIC bug, line 9
    return a

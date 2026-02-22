import os          # unused import (LINTING bug, line 1)
import json        # unused import (LINTING bug, line 2)

def add(a, b):      # fixed syntax
    return a + b

def divide(a, b):
    return a / b   # no zero division check (LOGIC bug, line 8)

def greet(name):
    message = "Hello"
    return message  # typo in variable name (LOGIC bug, line 12)
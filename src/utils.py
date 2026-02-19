import os          # unused import (LINTING bug, line 1)
import json        # unused import (LINTING bug, line 2)

def add(a, b)      # missing colon (SYNTAX bug, line 4)
    return a + b

def divide(a, b):
    return a / b   # no zero division check (LOGIC bug, line 8)

def greet(name):
    message = "Hello"
    return mesage  # typo in variable name (LOGIC bug, line 12)
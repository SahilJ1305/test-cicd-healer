import pandas as pd
import numpy as np
from collections import deque

def parse_data(data):
    return pd.DataFrame(data)

def calculate_mean(numbers):
    return np.mean(numbers)

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
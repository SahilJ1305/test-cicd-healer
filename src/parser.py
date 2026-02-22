import pandas as pd
import numpy as np
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def parse_data(data):
    return pd.DataFrame(data)

def calculate_mean(numbers):
    return np.mean(numbers)
import pandas as pd
import numpy as np
from collections import deque

def parse_data(data):
    return pd.DataFrame(data)

def calculate_mean(numbers):
    return np.mean(numbers)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
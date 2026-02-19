import pandas as pd
import numpy as np
from collections import deque

def parse_data(data):
    return pd.DataFrame(data)

def calculate_mean(numbers):
    return np.mean(numbers)
import pandas as pd          # not installed — IMPORT bug, line 1
import numpy as np           # not installed — IMPORT bug, line 2
from collections import Stack  # doesn't exist — IMPORT bug, line 3

def parse_data(data):
    return pd.DataFrame(data)

def calculate_mean(numbers):
    return np.mean(numbers)

from collections import Stack

def parse_data(data):
    return data  # Return raw data (or use alternative library like `csv`/`json` if needed)

def calculate_mean(numbers):
    # Pure-Python alternative to numpy.mean()
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
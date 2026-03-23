import os   
import math

def calculate_area(radius):
    if radius < 0:
        return None
    return math.pi * radius ** 2


def print_welcome_message():
    print("Welcome to the Autonomous DevOps Agent!")

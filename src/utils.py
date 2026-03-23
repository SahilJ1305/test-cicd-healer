import os
import math

def add(a, b):
    return a + b

def calculate_area(radius):
    if radius < 0:
        return None
    return math.pi * radius ** 2

def divide(a, b):
    if b == 0:
        return None
    return a / b

def print_welcome_message():
    print("Welcome to the Autonomous DevOps Agent!")
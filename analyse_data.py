import numpy as np
import sys

day = int(sys.argv[1])
print(f"day is {day}")

data = []
for i in range(-1, day):
    with open(f'.data/prices_round_1_day_{i}', 'r') as file:
        lines = file.readlines()
        data += lines


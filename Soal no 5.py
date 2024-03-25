"""
Nama : Nurul Aini
Nim : 221402005

"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file_path, 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

total_sum = sum(numbers)
formatted_sum = "{:,.3f}".format(total_sum)
print(formatted_sum)

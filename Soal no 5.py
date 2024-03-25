"""
Nama : Nurul Aini
Nim : 221402005

"""

with open("UTS/input.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

total_sum = sum(numbers)
formatted_sum = "{:,.3f}".format(total_sum)

print(formatted_sum)


"""
Nama : Nurul Aini
Nim : 221402005

"""
import datetime
current_year = datetime.datetime.now().year
days_this_year = (datetime.datetime(current_year + 1, 1, 1) - datetime.datetime(current_year, 1, 1)).days
whole_number = int(input("Enter a number: "))
result = whole_number / days_this_year
print(f"The result is: {result:.11f}")

"""
Nama : Nurul Aini
Nim : 221402005
"""
def calculate_product(number):
    product = 1
    for i in range(2, number + 1):
        product *= i
    return product

test_date = int(input("Masukkan tanggal ujian hari: "))
product = calculate_product(test_date)
print(f"The product of all values from 1 to {test_date} is: {product}")


"""
Nama : Nurul Aini
Nim : 221402005
"""
class BMI:
    def __init__(self, weight_pounds, height_feet):
        self.weight = weight_pounds
        self.height = height_feet

    def BMI_Value(self):
        height_meters = self.height * 0.3048  # ubah feet ke meter
        weight_kg = self.weight * 0.453592    # ubah pounds ke kilograms
        return weight_kg / (height_meters ** 2)

    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height


orang1 = BMI(170, 5.5)  # Berat 150 pound, tinggi 5.5 feet
orang2 = BMI(165, 5.8)  # Berat 160 pound, tinggi 5.7 feet

print("BMI orang 1:", orang1.BMI_Value())
print("BMI orang 2:", orang2.BMI_Value())

if orang1 == orang2:
    print("Keduanya memiliki berat dan tinggi yang sama.")
else:
    print("keduanya memiliki berat atau tinggi yang berbeda.")


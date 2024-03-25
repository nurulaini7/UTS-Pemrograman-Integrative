"""
Nama : Nurul Aini
Nim : 221402005
"""
import datetime

number_of_days = int(input("Masukkan tanggal hari ini: "))
future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
print("Tanggal yang berjarak", number_of_days, "hari dari sekarang adalah:", future_date.strftime("%A on %d %B %Y"))


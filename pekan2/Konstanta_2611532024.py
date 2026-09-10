#Buat file dengan nama Konstanta_2611532024.py
#Program ini menggunakan konstanta untuk menghitung luas lingkaran
#nama variabel ditambah 4 digit nim terakhir contoh: jari_12347



from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2024 = float(input('Masukkan nilai jari-jari: '))
luas_2024 = PI * jari_2024 * jari_2024
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2024, luas_2024))
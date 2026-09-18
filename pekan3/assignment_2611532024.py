# Buat file dengan nama assignment_2611532024.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2024 = int(input("Input angka-1: "))
angka2_2024 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2024)
print("Nilai angka2 =", angka2_2024)

# Assignment biasa
hasil_2024 = angka1_2024
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2024)

# Assignment penambahan
hasil_2024 = angka1_2024
hasil_2024 += angka2_2024
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_2024)

# Assignment pengurangan
hasil_2024 = angka1_2024
hasil_2024 -= angka2_2024
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2024)

# Assignment perkalian
hasil_2024 = angka1_2024
hasil_2024 *= angka2_2024
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2024)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2024 != 0:
    hasil_2024 = angka1_2024
    hasil_2024 /= angka2_2024
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2024)
    # Operator tambahan
    hasil_2024 = angka1_2024
    hasil_2024 //= angka2_2024
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2024)
    hasil_2024 = angka1_2024
    hasil_2024 %= angka2_2024
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2024)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_2024 = angka1_2024
hasil_2024 **= angka2_2024
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2024)
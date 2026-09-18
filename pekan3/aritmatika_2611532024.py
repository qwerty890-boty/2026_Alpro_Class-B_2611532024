# Buat file dengan nama aritmatika_2611532024.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2024 = int(input("Input angka-1: "))
angka2_2024 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2024 = angka1_2024 + angka2_2024
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2024)

# Pengurangan
hasil_2024 = angka1_2024 - angka2_2024
print("\nOperator Pengurangan")
print("Hasil =", hasil_2024)

# Perkalian
hasil_2024 = angka1_2024 * angka2_2024
print("\nOperator Perkalian")
print("Hasil =", hasil_2024)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2024 != 0:
    hasil_2024 = angka1_2024 / angka2_2024
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2024)

    hasil_2024 = angka1_2024 // angka2_2024
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2024)

    hasil_2024 = angka1_2024 % angka2_2024
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2024)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2024 = angka1_2024 ** angka2_2024
print("\nOperator Pangkat")
print("Hasil =", hasil_2024)
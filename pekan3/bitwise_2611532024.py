# Buat file dengan nama bitwise_2611532024.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n========================================")
print("3. OPERATOR BITWISE")
print("========================================")

angka1_2024 = int(input("Masukkan angka bitwise-1: "))
angka2_2024 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2024, "| biner =", bin(angka1_2024))
print("angka2 =", angka2_2024, "| biner =", bin(angka2_2024))

# Bitwise AND
hasil_2024 = angka1_2024 & angka2_2024
print("\nBitwise AND (&)")
print(angka1_2024, "&", angka2_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))

# Bitwise OR
hasil_2024 = angka1_2024 | angka2_2024
print("\nBitwise OR (|)")
print(angka1_2024, "|", angka2_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))

# Bitwise XOR
hasil_2024 = angka1_2024 ^ angka2_2024
print("\nBitwise XOR (^)")
print(angka1_2024, "^", angka2_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))

# Bitwise NOT
hasil_2024 = ~angka1_2024
print("\nBitwise NOT (~)")
print("~", angka1_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))

# Bitwise geser kiri
jumlah_geser_2024 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2024 = angka1_2024 << jumlah_geser_2024
print("\nBitwise geser kiri (<<)")
print(angka1_2024, "<<", jumlah_geser_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))

# Bitwise geser kanan
hasil_2024 = angka1_2024 >> jumlah_geser_2024
print("\nBitwise geser kanan (>>)")
print(angka1_2024, ">>", jumlah_geser_2024, "=", hasil_2024)
print("Biner hasil =", bin(hasil_2024))
print("Biner hasil (8 bit) =", format(hasil_2024, "08b"))
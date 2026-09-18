# Buat file dengan nama lainnya_2611532024.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan  identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2024 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2024 = [int(angka.strip()) for angka in input_data_2024.split(",")]

nilai_dicari_2024 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2024 = nilai_dicari_2024 in data_2024
print("\nOperator keanggotaan IN")
print(nilai_dicari_2024, "in", data_2024, "=", hasil_2024)

# Operator not in
hasil_2024 = nilai_dicari_2024 not in data_2024
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2024, "not in", data_2024, "=", hasil_2024)


print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_2024 = data_2024

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2024 = objek1_2024

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2024 = data_2024.copy()

print("objek1 =", objek1_2024)
print("objek2 =", objek2_2024)
print("objek3 =", objek3_2024)

# Operator is
hasil = objek1_2024 is objek2_2024
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2024)

# Operator is not
hasil_2024 = objek1_2024 is not objek3_2024
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2024)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2024 is objek3_2024)
print("objek1 == objek3 =", objek1_2024 == objek3_2024)
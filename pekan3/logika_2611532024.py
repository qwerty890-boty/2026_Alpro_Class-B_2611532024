# Buat file dengan nama logika_2611532024.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2024 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2024 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_2024)
print("A2 =", a2_2024)

# Konjungsi: bernilai True jika keduanya True
hasil_2024 = a1_2024 and a2_2024
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2024)

# Disjungsi: bernilai True jika salah satunya True
hasil_2024 = a1_2024 or a2_2024
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2024)

# Negasi A1: membalik nilai A1
hasil_2024 = not a1_2024
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2024)

# Negasi A2: membalik nilai A2
hasil_2024 = not a2_2024
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_2024)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2024 = a1_2024 != a2_2024
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_2024)
#Buat file dengan nama perulangan_for3_2611532024.py
#Buat program untuk perulangan for dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
#Program ini menggunakan fungsi input()

ulang_2024 = int(input("Masukkan jumlah perulangan: "))

jumlah_2024 = 0
for i in range(1, ulang_2024 + 1):
    print(i, end=" ")
    jumlah_2024 = jumlah_2024 + 1

    if i < ulang_2024:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_2024, end=" ")
print()
print("jumlah =", jumlah_2024)
    
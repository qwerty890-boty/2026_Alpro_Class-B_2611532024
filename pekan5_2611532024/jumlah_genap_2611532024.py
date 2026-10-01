#Buat file dengan nama jumlah_genap_2611532024.py
#Buat program untuk perulangan for dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
#Program ini menggunakan fungsi input()

ulang_2024 = int(input("Masukkan nilai batas: "))

jumlah_2024 = 0
for i in range (1, ulang_2024 + 1):
    if i % 2 == 0:
        print(i, end= " ")
        jumlah_2024 = jumlah_2024 + i

        if i < ulang_2024:
            print(" + ", end=" ")
        else:
            print(" = ", jumlah_2024, end=" ")
print()
print("Jumlah =", jumlah_2024)
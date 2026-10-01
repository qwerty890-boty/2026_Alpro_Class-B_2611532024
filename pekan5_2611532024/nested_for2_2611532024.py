#Buat file dengan nama nested_for2_2611532024.py
#Buat program untuk perulangan for dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
#Program ini menggunakan fungsi input()

batas_2024 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_2024 + 1):
    for j in range(1, batas_2024 + 1):
        print("*", end=" ")
    print() #pindah ke baris berikutnya

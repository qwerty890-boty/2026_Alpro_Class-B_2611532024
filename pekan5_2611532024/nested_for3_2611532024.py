#Buat file dengan nama nested_for3_2611532024.py
#Buat program untuk perulangan for dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
#Program ini menggunakan fungsi input()

batas_2024 = int(input("Masukkan nilai batas: "))
for i in range(batas_2024+1):
    for j in range(batas_2024+1):
        print(i+j, end=" ")
    print() #pindah ke baris berikutnya
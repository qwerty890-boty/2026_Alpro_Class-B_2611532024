#Buat file dengan nama nested_for4_2611532024.py
#Buat program untuk perulangan for dalam Python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
#Program ini menggunakan fungsi input()

tinggi_2024 = int(input("Masukkan tinggi pola (bilangan genap, misal 10: )"))

if tinggi_2024 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2024 = tinggi_2024
    c_2024 = a_2024
    lebar_2024 = (2 * tinggi_2024) - 2

    for i in range(1, tinggi_2024 + 1):
        b_2024 = c_2024 + 1

    for j in range(1, lebar_2024 + 1):

        #Baris atas dan bawah
        if i == 1 or j == tinggi_2024:
            if j == 1 or j == lebar_2024:
                print('#', end=" ")
            else:
                print("=", end= " ")

                #Baris isi
        else:
            if j == 1 or j == lebar_2024:
                print("|", end= " ")
            else:
                if j == c_2024:
                    print("<", end= " ")
                elif j == b_2024:
                    print(">", end= " ")
                elif j == (lebar_2024 - c_2024):
                    print("<", end= " ")
                elif j == (lebar_2024 - c_2024 + 1):
                    print(">", end= " ")
                elif j > b_2024 and j < (lebar_2024 - c_2024):
                    print(".", end= " ")
                else:
                    print(" ", end=" ")

        print()

        #Logika asli java
        a_2024 -= 2
        if a_2024 <= 0:
            c_2024 =(-a_2024) + 2
        else:
            c_2024 = a_2024
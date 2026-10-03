# Buat file dengan nama for_segitiga_2611532024.py
# Program menampilkan segitiga menggunakan perulangan for
# Nama variabel ditambah 4 digit terakhir NIM

tinggi_2024 = int(input("Masukkan tinggi segitiga: "))

for i_2024 in range(1, tinggi_2024 + 1):
    for spasi_2024 in range(tinggi_2024 - i_2024):
        print(" ", end="")

    for bintang_2024 in range(1, i_2024 + 1):
        print("*", end=" ")

    print()
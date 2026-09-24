#Buat file dengan nama multi_if1_2611532024.py
#Buat program untuk kondisional if
#Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
#Program ini menggunakan fungsi input()

umur_2024 = int(input("Input umur anda: "))
sim_2024 = input("Apakah Anda Sudah Punya Sim C (y/t:) ")[0]

if umur_2024 >= 17 and sim_2024 == 'y':
    print("Anda Sudah Dewasa dan Boleh bawa motor")

if umur_2024 >= 17 and sim_2024 != 'y':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")

if umur_2024 < 17 and sim_2024 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2024 < 17 and sim_2024 != 'y':
    print("Anda Belum Cukup Umur bawa motor")
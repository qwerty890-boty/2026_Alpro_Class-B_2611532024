#Buat file dengan nama Boolean_2611532024
#Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
#Deklarasi variabel dengan tipe data Boolean
is_lulus_2024=True
is_cumlaude_2024=True

#Menggunakan Boolean
nilai_2024=85
batas_lulus_2024=75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_2024=nilai_2024>=batas_lulus_2024 #Hasilnya akan True

print("=== Cek Kelulusan ===")
print("Nilai:", nilai_2024)
print("Apakah Lulus?:",status_kelulusan_2024)
if is_lulus_2024 and is_cumlaude_2024:
    print("Selamat, Anda lulus dnegan predikat Cumlaude")

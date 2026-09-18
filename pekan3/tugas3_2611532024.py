# ===SISTEM TRANSAKSI TOKO===
print("=== SISTEM TRANSAKSI TOKO ===")

# ===INPUT DATA PELANGGAN===
nama_2024 = input("\nMasukkan Nama Pelanggan : ")
status_2024 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
belanja_2024 = float(input("Masukkan Total Belanja : "))
jumlah_2024 = int(input("Masukkan Jumlah Barang : "))
promo_2024 = input("Masukkan Kode Promo : ").upper()

# ===DATA PROMO===
daftar_promo_2024 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# ===OPERATOR PERBANDINGAN===
belanja_minimum_2024 = belanja_2024 >= 200000
jumlah_minimum_2024 = jumlah_2024 >= 3
status_member_2024 = status_2024 == "member"

# ===OPERATOR KEANGGOTAAN===
promo_tersedia_2024 = promo_2024 in daftar_promo_2024
promo_tidak_tersedia_2024 = promo_2024 not in daftar_promo_2024
 
# ===OPERATOR LOGIKA===

# AND: member dan memenuhi minimum belanja
diskon_member_2024 = status_member_2024 and belanja_minimum_2024

# AND: jumlah barang memenuhi syarat dan promo tersedia
promo_khusus_2024 = jumlah_minimum_2024 and promo_tersedia_2024

# OR: mendapatkan promo jika memenuhi salah satu kondisi
mendapatkan_promo_2024 = diskon_member_2024 or promo_khusus_2024

# NOT: mengecek apakah pelanggan bukan member
bukan_member_2024 = not status_member_2024

# ===OPERATOR ARITMATIKA===
if diskon_member_2024:
    persentase_diskon_2024 = 0.10
else:
    persentase_diskon_2024 = 0.00

# Perkalian (*)
diskon_2024 = belanja_2024 * persentase_diskon_2024

# Pengurangan (-)
total_pembayaran_2024 = belanja_2024 - diskon_2024

# Pembagian (/)
rata_rata_2024 = belanja_2024 / jumlah_2024

# Modulus (%)
sisa_2024 = belanja_2024 % 1000

# ===OPERATOR PENUGASAN===
poin_2024 = 0

# Augmented assignment (+=)
poin_2024 += jumlah_2024

# Augmented assignment (-=)
if bukan_member_2024:
    poin_2024 -= 1

# ===HAK AKSES PELANGGAN===
member_access_2024 = status_member_2024
promo_access_2024 = promo_tersedia_2024
free_shipping_2024 = promo_2024 == "GRATISONGKIR"

# Membentuk kode hak akses
kode_hak_akses_2024 = 0

if member_access_2024:
    kode_hak_akses_2024 += 1

if promo_access_2024:
    kode_hak_akses_2024 += 2

if free_shipping_2024:
    kode_hak_akses_2024 += 4

# ===OPERATOR IDENTITAS===

# Membuat dua objek dengan nilai yang sama
kode_1_2024 = ["HEMAT10"]
kode_2_2024 = ["HEMAT10"]

# kode_3 menunjuk objek yang sama dengan kode_1
kode_3_2024 = kode_1_2024

identitas_sama_2024 = kode_1_2024 is kode_3_2024
identitas_berbeda_2024 = kode_1_2024 is not kode_2_2024

# == membandingkan nilai
nilai_sama_2024 = kode_1_2024 == kode_2_2024

# ===OPERATOR BITWISE===

# Nilai bit:
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

bit_member_2024 = 0b0001
bit_belanja_2024 = 0b0010
bit_jumlah_2024 = 0b0100
bit_promo_2024 = 0b1000

# OR (|) untuk menggabungkan status
kode_status_2024 = 0

if status_member_2024:
    kode_status_2024 = kode_status_2024 | bit_member_2024

if belanja_minimum_2024:
    kode_status_2024 = kode_status_2024 | bit_belanja_2024

if jumlah_minimum_2024:
    kode_status_2024 = kode_status_2024 | bit_jumlah_2024

if promo_tersedia_2024:
    kode_status_2024 = kode_status_2024 | bit_promo_2024

# AND (&) untuk memeriksa status tertentu
cek_member_2024 = kode_status_2024 & bit_member_2024
cek_promo_2024 = kode_status_2024 & bit_promo_2024

# XOR (^) untuk membandingkan dua kode
kode_referensi_2024 = 0b1011
perbandingan_status_2024 = kode_status_2024 ^ kode_referensi_2024

# SHIFT (<<)
hasil_shift_2024 = kode_status_2024 << 1

# OUTPUT DATA TRANSAKSI
print("\n")
print("=== DATA TRANSAKSI ===")

print("Nama Pelanggan       :", nama_2024)
print("Status Pelanggan     :", status_2024)
print("Total Belanja        : Rp" + str(int(belanja_2024)))
print("Jumlah Barang        :", jumlah_2024)
print("Kode Promo           :", promo_2024)

# OUTPUT HASIL VALIDASI
print("\n")
print("=== HASIL VALIDASI ===")

print("Belanja >= Rp200000        :", belanja_minimum_2024)
print("Jumlah Barang >= 3         :", jumlah_minimum_2024)
print("Status Member              :", status_member_2024)
print("Kode Promo Tersedia        :", promo_tersedia_2024)
print("Mendapatkan Diskon         :", diskon_member_2024)
print("Mendapatkan Promo          :", mendapatkan_promo_2024)

# OUTPUT HASIL PERHITUNGAN
print("\n")
print("=== HASIL PERHITUNGAN ===")

print("Diskon                  : Rp" + str(int(diskon_2024)))
print("Total Pembayaran        : Rp" + str(int(total_pembayaran_2024)))
print("Rata-rata Harga Barang  : Rp" + str(int(rata_rata_2024)))

# OUTPUT HAK AKSES PELANGGAN
print("\n")
print("=== HAK AKSES PELANGGAN ===")

print("Kode Hak Akses             :", kode_hak_akses_2024)
print("Member Access              :", member_access_2024)
print("Promo Access               :", promo_access_2024)
print("Free Shipping Access       :", free_shipping_2024)

# OUTPUT OPERASI BITWISE
print("\n")
print("=== OPERASI BITWISE ===")

print("=== Kode Status Transaksi ===")

print("0001 | 0010 | 0100 | 1000")

print("Kode Biner   :", format(kode_status_2024, "04b"))
print("Kode Desimal :", kode_status_2024)

# PEMERIKSAAN STATUS DENGAN AND
print("\n=== Pemeriksaan Status ===")

print("\nCek Member")
print(format(kode_status_2024, "04b"), "&", format(bit_member_2024, "04b"))

print("Hasil Biner   :", format(cek_member_2024, "04b"))
print("Hasil Desimal :", cek_member_2024)


print("\nCek Promo")
print(format(kode_status_2024, "04b"), "&", format(bit_promo_2024, "04b"))

print("Hasil Biner   :", format(cek_promo_2024, "04b"))
print("Hasil Desimal :", cek_promo_2024)

# PERBANDINGAN STATUS DENGAN XOR
print("\n=== Perbandingan Status ===")

print("Kode Transaksi :", format(kode_status_2024, "04b"))
print("Kode Referensi :", format(kode_referensi_2024, "04b"))

print(
    format(kode_status_2024, "04b"),
    "^",
    format(kode_referensi_2024, "04b")
)

print("Hasil Biner   :", format(perbandingan_status_2024, "04b"))
print("Hasil Desimal :", perbandingan_status_2024)
 
# SHIFT
print("\n=== Shift ===")

print(format(kode_status_2024, "04b"), "<< 1")

print("Hasil Biner   :", format(hasil_shift_2024, "b"))
print("Hasil Desimal :", hasil_shift_2024)

# OUTPUT OPERATOR IDENTITAS
print("\n=== OPERATOR IDENTITAS ===")

print("kode_1 is kode_3     :", identitas_sama_2024)
print("kode_1 is not kode_2 :", identitas_berbeda_2024)
print("kode_1 == kode_2     :", nilai_sama_2024)

# SELESAI
print("\n=== SELESAI ===")
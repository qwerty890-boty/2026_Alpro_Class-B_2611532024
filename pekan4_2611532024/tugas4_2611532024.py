# ============================================================
# SISTEM LOKET ALPRO ADVENTURE PARK
# Tugas 4 Algoritma dan Pemrograman
# ============================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ------------------------------------------------------------
# 1. INPUT DATA PENGUNJUNG
# ------------------------------------------------------------

nama_2024 = input("Masukkan Nama Pengunjung        : ")
umur_2024 = int(input("Input umur anda                 : "))
sim_2024 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()
jumlah_tiket_2024 = int(input("Masukkan jumlah tiket           : "))

# ------------------------------------------------------------
# 2. IF TUNGGAL
# Validasi jumlah tik
# ------------------------------------------------------------

if jumlah_tiket_2024 <= 0:
    print("Peringatan: kuota tiket tidak valid.")
    print("Program Selesai")
    exit()

# ------------------------------------------------------------
# 3. PEMILIHAN WAHANA MENGGUNAKAN MATCH-CASE
# ------------------------------------------------------------

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_2024 = int(input("Masukkan nomor paket (1-5)      : "))

match paket_2024:
    case 1:
        nama_wahana_2024 = "Wahana Safari Rimba"
        harga_satuan_2024 = 50000

    case 2:
        nama_wahana_2024 = "Wahana Arung Jeram"
        harga_satuan_2024 = 75000

    case 3:
        nama_wahana_2024 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2024 = 120000

    case 4:
        nama_wahana_2024 = "Wahana Roller Coaster Kilat"
        harga_satuan_2024 = 100000

    case 5:
        nama_wahana_2024 = "Wahana All-Access VIP"
        harga_satuan_2024 = 220000

    case _:
        print("Paket wahana tidak valid!")
        print("Program Selesai")
        exit()

# ------------------------------------------------------------
# Input data tambahan
# ------------------------------------------------------------

is_member_2024 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_2024 = input(
    "Apakah kode promo valid? (y/t)  : "
).strip().lower()

# ------------------------------------------------------------
# 4. VALIDASI IZIN KENDALI WAHANA
# Paket 3 menggunakan if-elif-else dengan AND dan !=
# Paket lainnya menggunakan if-else
# ------------------------------------------------------------

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2024 == 3:
    if umur_2024 >= 17 and sim_2024 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

    elif umur_2024 >= 17 and sim_2024 != 'y':
        print(
            "Status Akses: Anda sudah dewasa tetapi tidak boleh "
            "bawa motor ATV (wajib didampingi instruktur)."
        )

    elif umur_2024 < 17 and sim_2024 == 'y':
        print(
            "Status Akses: Identitas tidak valid: "
            "Belum cukup umur memiliki SIM."
        )

    else:
        print(
            "Status Akses: Anda belum cukup umur dan "
            "tidak boleh bawa motor ATV."
        )

else:
    if umur_2024 >= 10:
        print("Status Akses: Anda memenuhi batas usia wahana.")
    else:
        print("Status Akses: Anda belum memenuhi batas usia wahana.")

# ------------------------------------------------------------
# 5. PERHITUNGAN SUBTOTAL
# ------------------------------------------------------------

subtotal_2024 = harga_satuan_2024 * jumlah_tiket_2024

# ------------------------------------------------------------
# 6. AKUMULASI DISKON MENGGUNAKAN MULTI-IF
# Semua IF dibuat TERPISAH agar diskon dapat ditumpuk.
# ------------------------------------------------------------

total_diskon_persen_2024 = 0

# Diskon Belanja Besar
if subtotal_2024 >= 200000:
    total_diskon_persen_2024 += 10

# Diskon Member
if is_member_2024 in ['y', 'ya']:
    total_diskon_persen_2024 += 5

# Diskon Voucher Promo
if kode_promo_valid_2024 in ['y', 'ya']:
    total_diskon_persen_2024 += 15

# Diskon Tambahan Rombongan
if jumlah_tiket_2024 >= 5:
    total_diskon_persen_2024 += 5

# ------------------------------------------------------------
# 7. PERHITUNGAN PEMBAYARAN
# ------------------------------------------------------------

nominal_diskon_2024 = subtotal_2024 * (
    total_diskon_persen_2024 / 100
)

total_bayar_2024 = subtotal_2024 - nominal_diskon_2024

# ------------------------------------------------------------
# 8. EVALUASI KELULUSAN AUDIT MENGGUNAKAN IF-ELSE
# ------------------------------------------------------------

if total_bayar_2024 > 300000:
    catatan_layanan_2024 = (
        "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    )
else:
    catatan_layanan_2024 = "Terima kasih telah berkunjung."

# ------------------------------------------------------------
# 9. RINCIAN PEMBAYARAN
# ------------------------------------------------------------

print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_2024}")
print(f"Wahana           : {nama_wahana_2024}")
print(f"Jumlah Tiket     : {jumlah_tiket_2024}")
print(f"Subtotal Belanja : Rp {subtotal_2024:,.0f}")
print(
    f"Total Diskon     : {total_diskon_persen_2024}% "
    f"(Rp {nominal_diskon_2024:,.0f})"
)
print(f"Total Bayar      : Rp {total_bayar_2024:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2024}")

print("Program Selesai")
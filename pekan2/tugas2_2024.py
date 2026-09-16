from typing import Final

# ==========================================
# KONSTANTA
# ==========================================
BATAS_LULUS_2024: Final = 75.0


# ==========================================
# INPUT DATA PRAKTIKAN
# ==========================================
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2024 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2024 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_2024 = int(input("Masukkan Umur : "))
skor_tes_2024 = float(input("Masukkan Skor Tes Awal : "))


# ==========================================
# DATA TAMBAHAN
# ==========================================
alamat_2024 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

# Karakter
karakter_2024 = jenis_kelamin_2024[0]

# Bilangan kompleks sebagai token identifikasi
id_token_2024 = 100 + 3j


# ==========================================
# EVALUASI KELULUSAN
# ==========================================
status_lulus_2024 = skor_tes_2024 >= BATAS_LULUS_2024


# ==========================================
# MENAMPILKAN DATA DAN TIPE DATA
# ==========================================
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print(
    "Nama Mahasiswa :", nama_2024,
    "| Tipe :", type(nama_2024)
)

print(
    "Jenis Kelamin  :", karakter_2024,
    "| Tipe :", type(karakter_2024)
)

print("Alamat Domisili:")
print(
    alamat_2024,
    "| Tipe :", type(alamat_2024)
)

print(
    "Umur           :", umur_2024,
    "tahun | Tipe :", type(umur_2024)
)

print(
    "Skor Tes Awal  :", skor_tes_2024,
    "| Tipe :", type(skor_tes_2024)
)

print(
    "ID Token Sinyal:", id_token_2024,
    "| Tipe :", type(id_token_2024)
)


# ==========================================
# STATUS KELULUSAN
# ==========================================
print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print(
    "Batas Minimum Nilai :",
    BATAS_LULUS_2024
)

print(
    "Apakah Dinyatakan Lulus?:",
    status_lulus_2024,
    "| Tipe :",
    type(status_lulus_2024)
)
# ============================================================
# PROGRAM JAM PASIR KRISTAL PALINDROMIK
# PEKAN 5
# ============================================================

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK===")

# Input ukuran N
n_2024 = int(input("Masukkan ukuran skala jam pasir (N): "))


# ============================================================
# BORDER ATAS
# ============================================================

print("#", end="")

for angka_2024 in range(4 * n_2024 + 5):
    print("=", end="")

print("#")


# ============================================================
# FASE 1: JAM PASIR ATAS
# Baris N turun sampai 1
# ============================================================

for baris_2024 in range(n_2024, 0, -1):

    # Pembatas kiri
    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2024 in range(2 * (n_2024 - baris_2024)):
        print(" ", end="")

    # Angka menurun
    for angka_2024 in range(baris_2024, 0, -1):
        print(angka_2024, end="")
        print(" ", end="")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2024 in range(1, baris_2024 + 1):
        print(" ", end="")
        print(angka_2024, end="")

    # Spasi penyeimbang kanan
    for spasi_2024 in range(2 * (n_2024 - baris_2024)):
        print(" ", end="")

    # Pembatas kanan
    print(" ", end="")
    print("|", end="")

    # Pindah baris
    print()


# ============================================================
# FASE 2: POROS TITIK PUSAT
# ============================================================

print("|", end="")

# Spasi kiri
for spasi_2024 in range(2 * n_2024 + 1):
    print(" ", end="")

# Poros kristal
print("<*>", end="")

# Spasi kanan
for spasi_2024 in range(2 * n_2024 + 1):
    print(" ", end="")

# Pembatas kanan
print("|")



# ============================================================
# FASE 3: JAM PASIR BAWAH
# Baris 1 naik sampai N
# ============================================================

for baris_2024 in range(1, n_2024 + 1):

    # Pembatas kiri
    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2024 in range(2 * (n_2024 - baris_2024)):
        print(" ", end="")

    # Angka menurun
    for angka_2024 in range(baris_2024, 0, -1):
        print(angka_2024, end="")
        print(" ", end="")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2024 in range(1, baris_2024 + 1):
        print(" ", end="")
        print(angka_2024, end="")

    # Spasi penyeimbang kanan
    for spasi_2024 in range(2 * (n_2024 - baris_2024)):
        print(" ", end="")

    # Pembatas kanan
    print(" ", end="")
    print("|", end="")

    # Pindah baris
    print()


# ============================================================
# BORDER BAWAH
# ============================================================

print("#", end="")

for angka_2024 in range(4 * n_2024 + 5):
    print("=", end="")

print("#")
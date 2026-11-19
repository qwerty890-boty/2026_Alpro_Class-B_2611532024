LAST_DIGIT = 4  # Ganti nilai 0 dengan digit terakhir NIM Anda (d)
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Membaca 7 pengeluaran harian
for i in range(1, 8):
    pengeluaran = int(input(f"Day {i}: "))
    expenses.append(pengeluaran)
# Inisialisasi variabel perhitungan manual
total = 0
highest_val = expenses[0]
highest_day = 1
days_above_limit = 0
# Memproses data di dalam list expenses
for i in range(len(expenses)):
    nilai = expenses[i]
    total += nilai
    # Mencari pengeluaran tertinggi (mengambil hari pertama jika nilainya sama)
    if nilai > highest_val:
        highest_val = nilai
        highest_day = i + 1
    # Menghitung jumlah hari di atas daily_limit
    if nilai > daily_limit:
        days_above_limit += 1
# Menghitung rata-rata
average = total / 7
# Mencetak 5 baris output 
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_val})")
print(f"Days above limit: {days_above_limit}")

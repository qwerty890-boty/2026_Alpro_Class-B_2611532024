number_of_rows = 4
seats_per_row = 5

# Membuat denah 4 baris x 5 kursi dengan list berbeda untuk setiap baris
seats = [['.' for _ in range(seats_per_row)] for _ in range(number_of_rows)]
seats_taken = 0

while True:
    # Menampilkan denah kursi saat ini
    for i in range(number_of_rows):
        print(f"Row {i + 1}: {' '.join(seats[i])}")
    
    # Meminta input nomor baris
    row = int(input("Row (0 to stop): "))
    
    # Berhenti jika pengguna memasukkan 0
    if row == 0:
        break
        
    # Meminta input nomor kursi
    seat = int(input("Seat: "))
    
    # Validasi rentang baris dan kursi
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    # Cek apakah kursi sudah terisi ('X')
    elif seats[row - 1][seat - 1] == 'X':
        print("Seat already taken.")
    # Jika valid dan kosong, tandai kursi dengan 'X'
    else:
        seats[row - 1][seat - 1] = 'X'
        seats_taken += 1
        print("Seat booked.")

# Menampilkan total kursi yang berhasil dipesan di akhir program
print(f"Seats taken: {seats_taken}")

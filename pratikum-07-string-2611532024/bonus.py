# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: bonus

kalimat_uji = [
    "Kasur ini rusak",
    "Algoritma",
    "Kapak Masam"
]

for kalimat in kalimat_uji:
    teks_bersih = kalimat.replace(" ", "").lower()
    
    if teks_bersih == teks_bersih[::-1]:
        hasil = "Palindrome"
    else:
        hasil = "Not a palindrome"
        
    print(f'Kalimat: "{kalimat}" | Output: {hasil}')

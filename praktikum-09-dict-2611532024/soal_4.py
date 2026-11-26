daftar_kelas = input().split()
daftar_pengumpul = input().split()

set_kelas = set(daftar_kelas)
set_pengumpul = set(daftar_pengumpul)

jumlah_submit = len(set_pengumpul)
belum_mengumpulkan = set_kelas - set_pengumpul
jumlah_not_submit = len(set_pengumpul)

print(f"Submitted: {jumlah_submit} students")
print(f"Not Submitted: {jumlah_not_submit} students")

for nomor in range:
    if nomor not in set_pengumpul:
        print(nomor)
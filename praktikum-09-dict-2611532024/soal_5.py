n = int(input())
setoran_kas = {}
for i in range(n):
    baris = input().split()
    nama = baris[0]
    nominal =  int(baris[1])

    if nama in setoran_kas:
        setoran_kas[nama] += nominal
    else:
        setoran_kas[nama] = nominal

total_kas = 0
top_nama = ""
top_nominal = -1

for nama, total in setoran_kas.items():
    print(f"{nama}: {total}")
    total_kas += total

    if total > top_nominal:
        top_nominal = total
        top_nama = nama

print(f"Total Cash: {total_kas}")
print(f"Top contributor: {top_nama} ({top_nominal})")
    
    

    
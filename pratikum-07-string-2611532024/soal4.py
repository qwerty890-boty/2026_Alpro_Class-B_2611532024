# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: 4

phone = "081234567890"
jumlah_bintang = len(phone) - 7
masked = phone[:4] + ("*" * jumlah_bintang) + phone[-3:]
print(masked)

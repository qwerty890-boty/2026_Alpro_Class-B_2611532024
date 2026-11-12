# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: 7

nama_mhs = "ibnu brilliant" 
nim = "2611532024"

username = "ibnu" + nim[-3:]

angkatan = "20" + nim[:2]
nama = nama_mhs.title()

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)

print(f"{'Name':<10} : {nama}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {username}")
print(f"{'Intake':<10} : {angkatan}")

print("=" * 30)
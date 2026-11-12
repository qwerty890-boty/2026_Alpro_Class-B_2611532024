# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: 5

#A
username = input("Username: ")
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

#B
nim = input("NIM: ").strip()

if len(nim) == 10 and nim.isdigit():
    tahun_masuk = nim[:2]
    print(f"Valid, intake year 20{tahun_masuk}")
else:
    print("Invalid NIM.")



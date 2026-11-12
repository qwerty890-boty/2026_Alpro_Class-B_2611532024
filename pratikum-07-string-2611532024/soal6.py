# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "  Siti Aisyah  "
nim = "2610511023"
clean = full_name.strip()
space = clean.find(" ")

if space == -1:
  first_name = clean
else:
  first_name = clean[:space]

username = first_name.lower() + nim[-3:]
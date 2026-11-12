# Name: Ibnu Brilliant
# NIM: 2611532024
# Question: 3

#A
text = "Informatika"
print(text[10])
print(text.upper())
print(text)

#B
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)


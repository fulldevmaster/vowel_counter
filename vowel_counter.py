vowel = input("Enter a word: ")
count = 0
for i in vowel:
    if i in "aeiouAEIOU":
        count += 1
print("Count of vowel letter:", count)


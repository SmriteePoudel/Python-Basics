text = input("Enter a string: ")

vowel = 0
consonant = 0  

for ch in text:
    if ch in "aeiouAEIOU":
        vowel = vowel + 1
    else:
        consonant = consonant + 1

print("Vowels:", vowel)
print("Consonants:", consonant)
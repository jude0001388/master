#ask the user to enter a word
word = input("Enter a word: ")
word = word.upper()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count =0
consonant_count = 0
for letter in word:
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
            print("number of vowels in the word {number_of_vowels}")
            print("number of consonants in the word {number_of_consonants}")
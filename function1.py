def vowels_consonant(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count =0
    consonant_count = 0
    for letter in word:
            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"number of vowels in the word {vowel_count}")
    print(f"number of consonants in the word {consonant_count} ")


#main program
user_input = input("Enter a word: ")
#check if the user want to end the program
while user_input != "end":
#call the function with the user input
    vowels_consonant(user_input)
    user_input = input("Enter a word: ")
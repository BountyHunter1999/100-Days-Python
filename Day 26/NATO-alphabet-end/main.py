import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()

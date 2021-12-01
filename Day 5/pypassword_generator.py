import random
import string


LETTERS = [i for i in string.ascii_letters]
NUMBERS = list(str(range(0,10)))
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

characters = int(input("How many characters do u want ur password to be? "))

password = ""

for i in range(characters):
    password += random.choice(random.choice([LETTERS, NUMBERS, SYMBOLS]))

print(f"Here's your password of the {characters} length: ", password)
print(len(password))
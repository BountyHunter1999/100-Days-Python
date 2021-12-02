alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
total = len(alphabet)

def encode(word, shift):
    new_word = ''
    for i, l in enumerate(word):
        new_index = (alphabet.index(l) + shift) % total
        new_word += alphabet[new_index]
    return new_word

def decode(word, shift):
    new_word = ''
    for i, l in enumerate(word):
        new_index = (alphabet.index(l) - shift) % total
        new_word += alphabet[new_index]
    return new_word

if direction == 'encode':
    print(encode(word=text, shift=shift))
else:
    print(decode(word=text, shift=shift))
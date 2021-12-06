from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def encode_decode(word, shift, direction):
    new_word = ''
    encode = (direction == "encode")
    if not encode:
        shift *= -1
    for i, l in enumerate(word):
        if l in alphabet:
            new_index = (alphabet.index(l) + shift) % total
            new_word += alphabet[new_index]
        else:
            new_word += l

    return new_word

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    total = len(alphabet)

    print(encode_decode(word=text, direction=direction))

    con = input("Continue? Y or N: ").lower() == "y"
    if not con:
        break 


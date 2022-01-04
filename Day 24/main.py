# get the names
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    names = [name.strip() for name in names]

# Get the Letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.readlines()

# Save the letters in the folder "ReadyToSend".
for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as f:
        f.write("".join(letter).replace("[name]", name))


PLACEHOLDER = "[name]"

with open("/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("/Input/Names/invited_names.txt") as file:
    names = file.readlines(45)

for name in names:
    name = name.strip("\n")
    x = letter.replace(PLACEHOLDER, name)
    with open(f"/Output/ReadyToSend/letter_for_{name}.txt", mode='w') as file:
        file.write(x)


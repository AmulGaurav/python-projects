import cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in text:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if (new_position >= len(alphabet)) or (new_position < 0):
                new_position %= 26
            end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

flag = True

while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caeser(cipher_direction = direction, start_text = text, shift_amount = shift)
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if check != "yes":
        flag = False
        print("Goodbye")
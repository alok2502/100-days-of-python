from art import logo
print(logo)

alphabet_lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet_lists:
            output += letter
        else:
            shifted_position = alphabet_lists.index(letter) + shift_amount
            shifted_position %= len(alphabet_lists)
            output += alphabet_lists[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output}")

should_restart = True

while should_restart:
    direction = input("Enter if you want to encode or decode : ").lower()
    text = input("Enter the word you want to encrypt or decrypt : ").lower()
    shift = int(input("Enter letters to shift by number : "))
    ceaser(text, shift, direction)

    restart = input("Do you want to start it again? yes or no? ").lower()

    if restart == "no":
        should_restart = False
        print("Good Bye!!!")





from math import sqrt, ceil

from modules.constants import SUPPORTED_CHAR

def main():
    pass

def convert_user_input_to_number_array():
    """
    Converts plaintext to array of numbers.

    This function takes some user input and checks if all characters are 
    contained in the SUPPORTED_CHAR constant, should this be the case every
    character is mapped to a number in an array given by its index in
    SUPPORTED_CHAR + 2, as indices 0 and 1 cause issues.

    Returns
    -------
    array
        Contains a mapping number for every letter in the user input.
    """
    while True:
        print("Plaintext:", end=" ")
        plaintext = input()
        print("")
        plaintext_number_array = []
        for letter in plaintext:
            letter_index = SUPPORTED_CHAR.find(letter)
            if letter_index != -1:
                # Adding 2 to letter_index, as indices 
                # 0 and 1 cause issues in the later steps.
                plaintext_number_array.append(letter_index + 2)
            else:
                throw_non_supported_char_exception(letter) # TODO: add function
        return plaintext_number_array
    
def throw_non_supported_char_exception(non_supported_letter):
    """
    TODO: Write DOCSTRING
    """
    print(f"ERROR: '{non_supported_letter}' is not a valid letter")
    print(f"The program only works with the following letters:")
    for index, letter in enumerate(SUPPORTED_CHAR):
        # Displaying " " as [SPACE]
        if letter == " ":
            letter = "[SPACE]"
        # Formatting last letter with two newlines.
        if index + 1 == len(SUPPORTED_CHAR):
            print(letter, end="\n\n")
        else:
            print(letter, end=", ")
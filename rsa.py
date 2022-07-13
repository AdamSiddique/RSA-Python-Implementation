from math import sqrt, ceil

from modules.constants import SUPPORTED_CHAR

def main():
    convert_user_input_to_number_array()

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
                throw_non_supported_char_exception(letter)
                break
        return plaintext_number_array
    
def throw_non_supported_char_exception(non_supported_letter):
    """
    Prints error message regarding non supported characters.

    This function takes the non supported character found in 
    convert_user_input_to_number_array() and prints the character with some
    informative text that tells the user about the supported letters.

    Parameters
    ----------
    non_supported_letter : string
        Non supported letter to print.
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

def calculate_big_n_and_phi_big_n():
    """
    TODO: Write Docstring
    """
    # Receive prime numbers p and q until product bigger than SUPPORTED_CHAR.
    # TODO: Check if product needs to be bigger than SUPPORTED_CHAR + 2.
    while True:
        p, q = get_prime_numbers_p_and_q_from_user()
        big_n = p * q
        if big_n > len(SUPPORTED_CHAR):
            break
        else:
            print(f"ERROR: The product of p and q need to be bigger than {len(SUPPORTED_CHAR)}" +
                    "because of the amount of characters\n." +
                    "The current product of p and q is {big_n}",
                end="\n\n",
            )
    phi_of_big_n = (p - 1) * (q - 1)
    return big_n, phi_of_big_n

def get_prime_numbers_p_and_q_from_user():
    """
    TODO: Write Docstring
    """
    while True:
            print("Specify a prime number p: ")
            p = input()
            if p.isprime():
                break
            else:
                print(f"ERROR: {p} is not prime", end="\n\n")
    while True:
        print("Specify anoother prime number q: ")
        q = input()
        if q.isprime():
            break
        else:
            print(f"ERROR: {q} is not prime", end="\n\n")

def is_prime():
    """
    TODO: Write Docstring
    """
    pass
    


if __name__ == "__main__":
    main()
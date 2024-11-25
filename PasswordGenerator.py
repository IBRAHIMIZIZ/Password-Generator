import random

# The mapper dictionary provides leetspeak-style substitutions for each lowercase letter,
# mapping it to various possible character variants like uppercase letters, numbers, and symbols.
mapper = {
    "a": ("A", "a", "@", "4"),
    "b": ("B", "b", "8"),
    "c": ("C", "c"),
    "d": ("D", "d"),
    "e": ("E", "e", "3"),
    "f": ("F", "f"),
    "g": ("G", "g", "6"),
    "h": ("H", "h", "#"),
    "i": ("I", "i", "1", "!"),
    "j": ("J", "j"),
    "k": ("K", "k"),
    "l": ("L", "l", "1"),
    "m": ("M", "m"),
    "n": ("N", "n"),
    "o": ("O", "o", "0"),
    "p": ("P", "p"),
    "q": ("Q", "q", "9"),
    "r": ("R", "r"),
    "s": ("S", "s", "5", "$"),
    "t": ("T", "t", "7"),
    "u": ("U", "u"),
    "v": ("V", "v"),
    "w": ("W", "w"),
    "x": ("X", "x"),
    "y": ("Y", "y"),
    "z": ("Z", "z", "2")
}


def generatePassword():
    # Initialize the password as an empty string
    password = ""

    # Create a list to store words from the randomly chosen wordlist file
    wordslist = []

    # Open a random wordlist file (e.g., wordlist_1.txt, wordlist_2.txt, etc.)
    # and read its contents into wordslist
    # here there is only 24 wordlist
    with open(f"./Wordlists/wordlist_{random.randint(1,24)}.txt") as words:
        for i in words:
            # Remove any leading/trailing spaces or newline characters from each line
            wordslist.append(i.strip())

    # Desired password length (customizable)
    password_length = 21

    # Construct the password by randomly selecting words from the wordlist
    # Ensure that the password length doesn't exceed the specified length
    while len(password) != password_length:
        # Append a randomly selected word from the wordlist to the password
        password += wordslist[random.randint(0, len(wordslist) - 1)]

        # If the password exceeds the desired length, reset it to an empty string
        if len(password) > password_length:
            password = ""

    # Initialize an empty string for the shuffled password
    shuffled_password = ""

    # Iterate through each character in the password
    for i in password:
        # Map the character to a random variant (uppercase, symbol, or number) using the mapper
        shuffled_password += mapper[i][random.randint(0, len(mapper[i]) - 1)]

    # Return the final shuffled password along with company name (if exist)
    return "Company@" + shuffled_password


# Generate a password and print it along with its length
a = generatePassword()
print(a)

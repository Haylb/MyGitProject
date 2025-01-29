import random
import string


def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one of each type
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to make it more random
    random.shuffle(password)

    return ''.join(password)


# Get user input
try:
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")

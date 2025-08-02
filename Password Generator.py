import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password too short!"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter password length (min 4): "))
        print(f"Generated password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number.")

    again = input("Generate another? (y/n): ").lower()
    if again != 'y':
        break

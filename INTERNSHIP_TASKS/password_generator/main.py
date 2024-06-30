import random
import string

length = int(input("Enter the desired length of the password: "))

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(length)

print("Generated password:", password)

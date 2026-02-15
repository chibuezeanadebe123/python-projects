import random
import string

print("=== Password Generator ===")

length = int(input("How long should the password be? "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = ""

for _ in range(length):
    password += random.choice(all_characters)

print("\nYour password is:")
print(password)

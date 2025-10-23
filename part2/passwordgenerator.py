






import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter desired password length: "))
password = generate_password(length)
print(f"Your new password: {password}")



with open("passwords.txt", "a") as file:
    file.write(password + "\n")
print("Password saved to passwords.txt")

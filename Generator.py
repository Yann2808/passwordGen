import random
import string


def passwordGen (length) :
    # Les carctères possibles sont : les majuscules, les minuscules, les nombres et les ponctuations
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for i in range(length))

    return password


# Deamnder à l'utilisateur de rentrer une longueur souhaitée
length = int(input("Enter the length of the password: "))
password = passwordGen(length)
print("Password generated is : ", password)
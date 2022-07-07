import random


def random_password(password_count, password_len):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£&^$*(_)"
    for x in range(0, password_count):
        password = ""
        for i in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char

        print("Here's your password: ", password)


from random import randint, sample
from string import printable, whitespace


def gen_strong_password():
    length = int(input('Jak długie ma być hasło (od 8 do 32 znaków): '))
    password = ''.join(sample(printable.replace(whitespace, ''), length))
    # password = ''.join(string.printable.replace(string.whitespace, '') for random.choice in range(length))
    return password


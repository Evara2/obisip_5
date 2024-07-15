"""Password generator allows you to generate a random password of length N."""
from random import choice, shuffle
from string import ascii_letters, digits, punctuation


def password_generator(length=8):
    """
    >>> len(password_generator())
    8
    >>> len(password_generator(length=16))
    16
    >>> len(password_generator(257))
    257
    >>> len(password_generator(length=0))
    0
    >>> len(password_generator(-1))
    0
    """
    chars = tuple(ascii_letters) + tuple(digits) + tuple(punctuation)
    return "".join(choice(chars) for x in range(length))


def alternative_password_generator(ctbi, i):

    i = i - len(ctbi)
    quotient = int(i / 3)
    remainder = i % 3
    chars = (
        ctbi
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    chars = list(chars)
    shuffle(chars)
    return "".join(chars)



def random(ctbi, i):
    return "".join(choice(ctbi) for x in range(i))


def random_number(ctbi, i):
    pass  


def random_letters(ctbi, i):
    pass 


def random_characters(ctbi, i):
    pass  


def main():
    length = int(input("Please indicate the max length of your password: ").strip())
    ctbi = input(
        "Please indicate the characters that must be in your password: "
    ).strip()
    print("Password generated:", password_generator(length))
    print(
        "Alternative Password generated:", alternative_password_generator(ctbi, length)
    )
    print("[If you are thinking of using this passsword, You better save it.]")


if __name__ == "__main__":
    main()
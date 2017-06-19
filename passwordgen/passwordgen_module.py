import random


def passwordgen(password=None):
    result = ""
    for i in range(8):
        result += chr(random.randint(33, 126))
    return result


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()


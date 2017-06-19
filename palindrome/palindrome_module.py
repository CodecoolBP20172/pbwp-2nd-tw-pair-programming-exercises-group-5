a=str
def palindrome(word):
    if str(word[::-1].lower().replace(" ", "")) == str(word).lower().replace(" ", ""):
        return True
    else:
        return False


def main():
    palindrome(a)
    return


if __name__ == '__main__':
    main()

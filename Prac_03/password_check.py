def main():
    password = input("Enter a password: ")
    password = get_password(password)
    change_asterisk(password)


"""Change password to asterisk"""


def change_asterisk(password):
    for char in range(len(password)):
        print('*', end='')


"""Check to see if password has valid length."""


def get_password(password):
    while len(password) < 5 or len(password) > 12:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


if __name__ == '__main__':
    main()

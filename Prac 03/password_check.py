def main():
    password = input("Enter a password: ")
    while len(password) < 5 or len(password) > 12:
        print("Invalid password")
        password = input("Enter a password: ")
    for char in range (len(password)):
        print('*', end='')

if __name__ == '__main__':
    main()
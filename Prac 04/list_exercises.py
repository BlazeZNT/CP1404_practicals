def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter a user name: ")
    while username not in usernames:
        print("Access Denied")
        username = input("Enter a user name: ")
    else:
        print("Acces Grated")
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        while number <= 0:
            print("invalid number. Please try again")
            print("--------------")
            number = int(input("Enter a number: "))
        numbers.append(number)
    print(numbers)
    print("The last number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest numbmer is {}".format(min(numbers)))
    print("The largerst numbmer is {}".format(max(numbers)))
    print("The average number is {}".format(calculate_average(numbers)))

def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    return average
if __name__ == '__main__':
    main()
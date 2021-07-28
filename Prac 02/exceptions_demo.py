def main():
    """
    CP1404/CP5632 - Practical
    Answer the following questions:
    1. When will a ValueError occur?
    2. When will a ZeroDivisionError occur?
    3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    """

    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

if __name__ == "__main__" :
    main()

    #number 1 answer : The ValueError occurs when the input is not a valid interger example .a , 10.50.
    #number 2 answer : The ZeroDivisionError occurs when the input of the denominator becomes zero.
    #number 3 answer : the input of the values can be changed to float instead of nubmer to allow more room.
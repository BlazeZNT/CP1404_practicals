def main():
    Name_file = "name.txt"
    name_file = open("Name_file","w")
    user_name = input("Please enter a name :")
    print("Your name is {}".format(user_name),file=name_file)

    number_read = open("numbers.txt","r")
    first_line_read = int(number_read.readline())
    second_line_read = int(number_read.readline())
    add = first_line_read + second_line_read
    number_read.close()
    print("{}".format(add),file=name_file)

    number_read = open("numbers.txt", "r")
    total = 0
    for number in number_read:
        each_line= int(number)
        total= total+ each_line
    print("{}".format(total),file=name_file)

if __name__ == "__main__":
    main()
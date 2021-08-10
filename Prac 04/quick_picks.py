import random
minium = 1
maximum = 45
maximum_number_in_line = 6
def main():
    times_picks = int(input("How many quick picks? : "))
    while times_picks <= 0 :
        print("invalid number . Please try again")
        times_picks = int(input("How many quick picks? : "))
    for i in range(times_picks):
        quick_picks = []
        for j in range(maximum_number_in_line):
            number = random.randint(minium,maximum)
            while number in quick_picks:
                number = random.randint(minium,maximum)
            quick_picks.append(number)
        quick_picks.sort()
        print(quick_picks)






if __name__ == '__main__':
    main()
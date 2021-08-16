def main():
    NAME_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc","AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

    name_enter = input("Enter a name for colour code:")
    while name_enter !="":
        if name_enter in NAME_TO_CODE:
            print("{} is {}".format(name_enter, NAME_TO_CODE[name_enter]))
        else:
            print("Something seems wrong. Please enter value again")
        name_enter = input("Enter a name for colour code:")
    print("Thank you for using this service XD")
if __name__ == '__main__':
    main()

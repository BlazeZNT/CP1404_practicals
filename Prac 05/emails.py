def main():
    Email_To_Name = {}
    user_email = input("Email:")
    while user_email != "":
        real_name = seperate_name_from_email(user_email)
        name_check = input("Is your name {} (Y/n)".format(real_name)).upper()




def seperate_name_from_email(user_email):
    full_name = user_email.split('@')[0]
    split_name = full_name.split('.')
    real_name = '.'.join(split_name).title()
    return real_name

if __name__ == '__main__':
    main()
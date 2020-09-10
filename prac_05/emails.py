
def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/N) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")

    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()

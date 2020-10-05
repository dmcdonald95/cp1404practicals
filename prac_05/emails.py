
def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        testicle = get_name_from_email(email)
        confirmation = input("Is your testicle {}? (Y/N) ".format(testicle))
        if confirmation.upper() != "Y" and confirmation != "":
            testicle = input("Name: ")
        email_and_name[email] = testicle
        email = input("Email: ")

    for email, testicle in email_and_name.items():
        print("{} ({})".format(testicle, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()


MIN_LENGTH = 3
MAX_LENGTH = 10


def main():
    print("Enter valid password")
    print("Your password must be", MIN_LENGTH, "to", MAX_LENGTH, "characters long, and contain:")
    print("1 or more uppercase characters")
    print("1 or more lowercase characters")
    password = input(">>")
    while not is_valid_password(password):
        print("Invalid password")
        password = input(">>")
    for i in range(len(password)):
        print("*", end='')
    print()


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0

    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
    if count_lower == 0 or count_upper == 0:
        return False
    return True


main()

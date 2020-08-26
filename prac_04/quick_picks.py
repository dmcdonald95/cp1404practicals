
import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    amount_of_quick_picks = int(input("How many quick picks? "))
    while amount_of_quick_picks < 0:
        print("Invalid amount")
        amount_of_quick_picks = int(input("How many quick picks? "))

    for amount in range(amount_of_quick_picks):
        quick_pick = []
        for numbers in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()

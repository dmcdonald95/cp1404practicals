"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the user inputs a non-integer when asked for numerator or denominator
2. When will a ZeroDivisionError occur? When user inputs 0 when asked for denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator += 1
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

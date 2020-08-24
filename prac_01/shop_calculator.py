
total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
else:
    for i in range(number_of_items):
        item_price = float(input("Price of item: $"))
        total_price += item_price
    if total_price > 100:
        total_price *= 0.9
    print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))

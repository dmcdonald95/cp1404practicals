OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')
name = input("Enter name here: ")
print(name, file=out_file)
out_file.close()

in_file = open(OUTPUT_FILE, 'r')
read_name = in_file.read()
print("Your name is: ", read_name)
in_file.close()

in_file = open("numbers.txt", 'r')
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(number_one + number_two)

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = (int(line))
    total += number
in_file.close()
print(total)


from prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 01", 100)
    my_taxi.drive(40)
    print(my_taxi, "${:.2f}".format(my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi, "${:.2f}".format(my_taxi.get_fare()))


main()


from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    my_silver_taxi.drive(18)
    print(my_silver_taxi)
    print("${:.2f}".format(my_silver_taxi.get_fare()))


main()

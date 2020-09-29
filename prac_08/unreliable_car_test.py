
from prac_08.unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("The Red Rocket", 100, 10)
    my_reliable_car = UnreliableCar("Lightning McQueef", 100, 90)

    for attempt in range(1, 12):
        print("Attempting to drive {}km:".format(attempt))
        print("{:12} drove {:2}km".format(my_reliable_car.name, my_reliable_car.drive(attempt)))
        print("{:12} drove {:2}km".format(my_unreliable_car.name, my_unreliable_car.drive(attempt)))

    print(my_reliable_car)
    print(my_unreliable_car)


main()

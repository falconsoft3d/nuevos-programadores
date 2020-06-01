class Car():

    def displacement(self):
        print("I go using 4 wheels")


class Moto():

    def displacement(self):
        print("I go using 2 wheels")


class Truck():

    def displacement(self):
        print("I go using 6 wheels")


def find_out_displacement(vehicle):
    vehicle.displacement()


my_vehicle = Moto()
find_out_displacement(my_vehicle)

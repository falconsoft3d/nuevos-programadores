
class Vehicle():
    def __init__(self, pmake, pmodel):
        self.make = pmake
        self.model = pmodel
        self.on = False
        self.acelerate = False
        self.brakes = False

    def start(self):
        self.on = True

    def to_acelerate(self):
        self.acelerate = True

    def to_brake(self):
        self.brakes = True

    def status(self):
        print("Make ", self.make, "\nModel ", self.model)


class Moto(Vehicle):
    pass


my_moto = Moto("Jawa", "350")
print(my_moto.status())

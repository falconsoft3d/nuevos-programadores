
class Vehicle():
    def __init__(self, pmake, pmodel):
        self.make = pmake
        self.model = pmodel
        self.on = False
        self.accelerate = False
        self.brakes = False

    def start(self):
        self.on = True

    def to_acelerate(self):
        self.acelerate = True

    def to_brake(self):
        self.brakes = True

    def status(self):
        print("Make ", self.make, "\nModel ", self.model, "\nOn ", self.on, "\nAceclerate ", self.accelerate,
              "\nBrakes ", self.brakes)

# ----------------------------------- Class Van -------------------------------------------------------


class Van(Vehicle):
    def to_load(self, pload):
        self.load = pload
        if self.load:
            return "The van is loaded"
        else:
            return "The van is not loaded"

# ----------------------------------- Class Moto -------------------------------------------------------


class Moto(Vehicle):
    jump = ""
    def to_jump(self):
        self.jump = "This moto is jumping"

    def status(self):
        print("Make ", self.make, "\nModel ", self.model, "\nOn ", self.on, "\nAceclerate ", self.accelerate,
              "\nBrakes ", self.brakes, "\nJump ", self.jump)


# ----------------------------------- Class Electric Vehicle -------------------------------------------------------


class VElectric():
    def __init__(self):
        self.autonomy = True

    def charge(self):
        self.charging = True


print("\nMoto features")
my_moto = Moto("Jawa", "350")
my_moto.to_jump()
print(my_moto.status())

print("Van features")
my_van = Van("Opel", "Corsa")
my_van.start()
my_van.status()
print(my_van.to_load(True))


# ----------------------------------- Class EBike -------------------------------------------------------

class Ebike(VElectric, Vehicle):
    pass

my_bike = Ebike()
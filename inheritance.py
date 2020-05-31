
class Car():
    def __init__(self):
        self.__chassis_lenght = 250
        self.__chassis_width = 120
        self.__wheels = 4
        self.__on = False

    def start(self, decision):
        self.__on = decision

        if (self.__on):
            checked = self.__interal_check()

        if (self.__on and checked):
            return "The car is on"
        elif (self.__on and checked == False):
            return "Something went wrong during internal check"
        else:
            return "The car is off"

    def status(self):
        print("The car has ", self.__wheels, " wheels. It's width is ", self.__chassis_width,
              " and it's lenght is about ", self.__chassis_lenght)

    def __interal_check(self):
        print("Checking all features")
        self.fuel = "ok"
        self.oil = "ok"
        self.doors = "close"

        if self.fuel == "ok" and self.oil == "ok" and self.doors == "close":
            return True
        else:
            return False


my_car = Car()
print(my_car.start(True))
print(my_car.status())

print("-----------------Second car will be here-------------------")

second_car = Car()
print(second_car.start(False))
print(second_car.status())
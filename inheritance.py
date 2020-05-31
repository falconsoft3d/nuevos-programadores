
class Car():
    def __init__(self):
        self.__chassis_lenght = 250
        self.__chassis_width = 120
        self.__wheels = 4
        self.__on = False

    def start(self, decision):
        self.on = decision

        if (self.on):
            return "The car is on"
        else:
            return "The car is off"

    def status(self):
        print("The car has ", self.__wheels, " wheels. It's width is ", self.__chassis_width,
              " and it's lenght is about ", self.__chassis_lenght)


my_car = Car()
print(my_car.start(True))
print(my_car.status())

print("-----------------Second car will be here-------------------")

second_car = Car()
print(second_car.start(False))
print(second_car.status())

class Car():
    chassis_lenght = 250
    chassis_width = 120
    wheels = 4
    on = False

    def start(self):
        self.on = True

    def status(self):
        if self.on:
            return "The car is on"
        else:
            return "The car is off"

my_car = Car()

print("The lenght of the car is: " + str(my_car.chassis_lenght))
print("The car has: " + str(my_car.wheels) + " wheels")

my_car.start()
print(my_car.status())

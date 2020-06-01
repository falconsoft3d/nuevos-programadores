class Person():

    def __init__(self, pname, page, presidence):
        self.name = pname
        self.age = page
        self.residence = presidence

    def description(self):
        print("Name: ", self.name, " Age: ", self.age, " Residence: ", self.residence)


class Worker(Person):

    def __init__(self, psalary, pseniority, pname, page, presidence):

        super().__init__(pname, page, presidence)
        self.salary = psalary
        self.seniority = pseniority

    def description(self):
        super().description()
        print("Salary : ", self.salary, " Seniority: ", self.seniority)


first_worker = Worker(500, 10, "Ernesto", 33, "Spain")
first_worker.description()

print("Is this a worker? " + str(isinstance(first_worker, Worker)))
print("Is this a Person? " + str(isinstance(first_worker, Person)))

print("-----------------Second use of isinstance-----------------")
second_worker = Person("Antonio", 40, "Spain")
second_worker.description()
print("Is this a worker? " + str(isinstance(second_worker, Worker)))
print("Is this a Person? " + str(isinstance(second_worker, Person)))
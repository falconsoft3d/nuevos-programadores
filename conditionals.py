president_salary = int(input("Type salary of the president"))
print("The salary of the president is" + str(president_salary))

principal_salary = int(input("Type salary of the principal"))
print("The salary of the president is" + str(principal_salary))

manager_salary = int(input("Type salary of the manager"))
print("The salary of the president is" + str(manager_salary))

worker_salary = int(input("Type salary of the worker"))
print("The salary of the president is" + str(manager_salary))

if worker_salary < manager_salary < principal_salary < president_salary:
    print("Everything works fine")
else:
    print("Something is going wrong")





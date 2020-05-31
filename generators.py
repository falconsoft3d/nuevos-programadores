print("First exercise")


def even_number(limit):
    num = 1
    my_list = []
    while num < limit:
        my_list.append(num*2)
        num = num+1
    return my_list


print(even_number(10))

print("Second exercise with generator \n")


def even_number_generator(limit):
    num = 1
    while num < limit:
        yield num*2
        num = num+1


result = even_number_generator(10)
print(next(result))
print("We could have more code here")
print(next(result))
print("We could have more code here")
print(next(result))
print("We could have more code here")

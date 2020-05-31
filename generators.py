
def get_cites(*cities):
    for elements in cities:
       # for subelement in elements:
        yield from elements


result = get_cites("Madrid", "Barcelona", "Valencia", "Aragon")
print(next(result))
print(next(result))
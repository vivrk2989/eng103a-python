car = {'Tesla', 'Mercedes', 'Range Rover'}

print(car, type(car))

car.add("Tata")

print(car)


# Sets are mutable and unordered

car.discard('Tesla')

print(car)

car.add('Tesla')
car.add('Tesla')

print(car)


# Sets give us the unique value


# Frozen set

x = frozenset(['let', 'it', 'go'])
print(x)

# Frozen sets are immutable sets




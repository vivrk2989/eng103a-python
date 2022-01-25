# Dictionaries

my_dict = {'key': 'value'}

table = {
    'name': 'The Table',
    'colour': 'light brown',
    'dimensions': {
        'height': 120,
        'length': 200,
        'width': 150
    }
}

print(table.get('dimensions').get('width')) # or print(table['dimensions']['width'])
print(table['dimensions']['width'])
print(table)
print(table['colour']) # Dictionary name [ KEY ]

table['height'] = 125 # changes the initial value given in the beginning
table['price'] = 99.99 # Adds another key to the dictionary

table.update({'price': 99.99, 'height': 125})

print(table)


print(table.get('legs'), 'Key Missing')
# print(table['legs'])

print(table)
print(table.keys())  # gives us the keys
print(table.values())  # gives us the values
print(table.items())  # gives us both keys and values











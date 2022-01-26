# # Lists
#
# shopping_list = ["eggs", "bread", "bananas", "tea"]
# print(shopping_list, type(shopping_list))
#
# print(len(shopping_list))
#
# print(shopping_list[0])
# print(shopping_list[-1])
#
# shopping_list[2] = "milk"
# print(shopping_list)
# # shopping_list[4] = "biscuits"
#
# shopping_list.append("biscuits")
# print(shopping_list)
#
# shopping_list.append("bread")
# shopping_list.append("bread")
# print(shopping_list)
#
# shopping_list.remove("bread")
# print(shopping_list)
#
# last_item = shopping_list.pop()
# print(shopping_list)
# print(last_item)

# mixed = [1, 2, "three", True, None, ["another", "list"], 6, 7, 8, 8]
# print(mixed)

# mixed[1] = 2.0
# print(mixed)
#
# # Lists are mutable
#
# print(mixed[2:7:2])  # going two steps at a time
# print(mixed[7:2:-1]) # going one step behind starting from 7
# print(mixed[::3]) # going three steps starting from the oth position till the end of the list

# # print(mixed[5][0][0])
#
# sublist = mixed[5]
# print(sublist)
# mixed[5][1] = 'b'
# print(mixed)
# print(sublist)

# #Tuples
#
# colours = ("red", "red", "blue", "green")
# print(colours, type(colours))
#
# print(colours[0])
# # colours[0] = "maroon"
#
# # Tuples are IMMUTABLE
#
# print(colours.count("red"))
# print(colours.index("green"))
#
# list_in_tuple = (
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# )
#
# print(len(list_in_tuple))
#
# list_in_tuple[0].append("SUCCESS")
#
# print(list_in_tuple)



# Split

text = 'It was the best of times'

text_list = text.split(" ")  #Splitting based on the the space
print(text_list, type(text_list))

csv = "12,235,3256,456,67,78"
csv_list = csv.split(",")
print(csv_list)

# Join

print("---".join(text_list))
print("".join(csv_list))


n = [56, 32, 56, 678, 23, 1, 0]

print(n)
n.sort()
print(n)


# Look into this later











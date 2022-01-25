# # def woof(number_of_woofs):
# #     for i in range(number_of_woofs):
# #         print("Woof!")
# #
# # woof(17)
#
# def woof(number_of_woofs):
#     print("Woof!" * number_of_woofs)
#
# woof(2)
#
# def greeting(name):
#     print(f"Hello to you, {name}")
#
# greeting("Vivek")

# def double_plus_one(num1, num2):
#     ans = (num1 * 2) + num2
#     return ans
#
# print(double_plus_one(5, 2))

# def double_plus_one(num1, num2=1):   # This works well
#     ans = (num1 * 2) + num2
#     return ans
#
# print(double_plus_one(5, 2))
# print(double_plus_one(5))


# def double_plus_one(num1 = 1, num2):   # This wont work
#      ans = (num1 * 2) + num2
#      return ans
#
# print(double_plus_one(5, 2))
# print(double_plus_one(5))


# def shopping(*items):  #multiargs   # considers it as a tuple
#     print(items, type(items))
#
# shopping("banana", "apple", "orange")

# def shopping(*items): #multiargs   # considers it as a tuple
#     for item in items:
#         print(f"Don't forget to buy a {item}")

# def shopping(name, *items): #multiargs
#     for item in items:
#         print(f"{name}! Don't forget to buy a {item}")
#
# shopping("Vivek", "banana", "apple", "orange")

# def shopping(name, *items, shout=False): #multiargs
#     if shout:
#         name = name.upper()
#     for item in items:
#         print(f"{name}! Don't forget to buy a {item}")
#
# shopping("Vivek", "banana", "apple", "orange", shout=True) # using shout i get my name in caps

# def greeting(name):
#     print(f"Hello to you, {name}")
#
# greeting("Vivek")
#
# greeting(2345)

#
# #Type Hints
#
# def greeting(name:str):
#      print("Hello to you, " + name)
#
# greeting("Vivek")
# greeting(2345)


# def greeting(name: str = "Vivek"):
#     print("Hello to you, " + name)
#
#
# greeting()


# def double_plus_one(num1: int, num2: int) -> int:  # Type in for the output i.e. the output should be integer
#     ans = (num1 * 2) + num2
#     return ans
#
# x = double_plus_one(5, 6)
# print(x)

#Look into Positional Arguments

# Functions should have clear names seperated with underscores

# Any function that doesnt return anything, it automatically return None

# Keep your functions small

# Use comments for functions


def add_user():
    """
    Create a new user.
    Prompt for name and email address
    Store in databse
    """
    pass

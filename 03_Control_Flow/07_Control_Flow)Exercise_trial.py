# print("\nQ1b\n")
# # Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# # A1b:
# for number in x:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print()

# # print("\nQ1c\n")
# # Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# for number in x[0:5]:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print()


# # print("\nQ2a\n")
# # # Q2a: from the list of names, create another list that consists of only the first letters of each first name
# # # e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
#
# # A2a:
#
# First_letter = []
#
# for name in names:
#
# print(First_letter)


print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# # A3a:
#
#
# set_with_no_duplicates = []
# for x in list_of_lists:
#     if len(x) == len(set(x)):
#         set_with_no_duplicates.append(x)
#
# print(set_with_no_duplicates)


user_input = True
Enter_a_number = int(input("Enter a number greater than 100:"))

while user_input:
    if Enter_a_number > 100:
        print(Enter_a_number)
    else:
        print("Number not greater than 100")









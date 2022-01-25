# Basic version

# For the numbers 1 to 100
# Play FizzBuzz
# Print the number
# If divisible by 3, Fizz
# If by 5, buzz
# If both, fizzbuzz

# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)


# What can you add?
# Can we customize (having as a variable) the end number?
# Or the start number?
# Can we get those from player input?
# Can we input alternate words for fizz and buzz?


# Game with user inputs

# Start_number = int(input('start value\n'))  # User input for start number
# End_number = int(input('End value\n'))  #User input for end number
#
div_by_3 = input('How would you want to describe the number if divisible by 3?\n')  #User input for the word if number is divisible by 3
div_by_5 = input('How would you want to describe the number if divisible by 5?\n')  #User input for the word if number is divisible by 5
div_by_3_and_5 = input('How would you want to describe the number if divisible by both 3 and 5?\n')  #User input for the word if number is divisible by both 3 and 5
div_by_7 = input('How would you want to describe the number if divisible by 7?\n')  # User input for the word if the number is divisible by 7

user_input = True

while user_input:
    Start_number = (input('start value\n'))
    End_number = (input('End value\n'))
    if Start_number.isdigit() and End_number.isdigit():
        for number in range(int(Start_number), int(End_number) + 1):
            if number % 3 == 0 and number % 5 == 0:  # If number is a multiple of both 3 and 5
                print(div_by_3_and_5)
            elif number % 3 == 0:  # If the number is a multiple of 3
                print(div_by_3)
            elif number % 5 == 0:  # If the number is a multiple of 5
                print(div_by_5)
            elif number % 7 == 0:  # If the number is a multiple of 7
                print(div_by_7)
            else:
                print(number)  # If it doesnt satify any of the above

# for number in range(Start_number, End_number +1):
#     if number % 3 == 0 and number % 5 == 0:  # If number is a multiple of both 3 and 5
#         print(div_by_3_and_5)
#     elif number % 3 == 0:  # If the number is a multiple of 3
#         print(div_by_3)
#     elif number % 5 == 0:  # If the number is a multiple of 5
#         print(div_by_5)
#     elif number % 7 == 0:  # If the number is a multiple of 7
#         print(div_by_7)
#     else:
#         print(number)  # If it doesnt satify any of the above cases, we simply print this number

# prime_number = input('How would you want to describe the number if it is prime?\n')  #User input for the word if the number is prime
#
# # Finding the prime numbers in the given range
# for num in range(Start_number, End_number + 1):
#     if num > 1:  #Prime numbers are greater than 1. 1 is neither prime nor composite
#         for p in range(2,num):
#             if (num % p) == 0:
#                 break
#         else:
#             print(f"{num} is a {prime_number}")





# Game with user inputs for start and end number and also buzz word choice

# Start_number = int(input('start value\n'))  # User input for start number
# End_number = int(input('End value\n'))  #User input for end number
#
# div_by_3 = input('How would you want to describe the number if divisible by 3?\n')  #User input for the word if number is divisible by 3
# div_by_5 = input('How would you want to describe the number if divisible by 5?\n')  #User input for the word if number is divisible by 5
# div_by_3_and_5 = input('How would you want to describe the number if divisible by both 3 and 5?\n')  #User input for the word if number is divisible by both 3 and 5
# div_by_7 = input('How would you want to describe the number if divisible by 7?\n')  # User input for the word if the number is divisible by 7
#
# for number in range(Start_number, End_number +1):
#     if number % 3 == 0 and number % 5 == 0:  # If number is a multiple of both 3 and 5
#         print(div_by_3_and_5)
#     elif number % 3 == 0:  # If the number is a multiple of 3
#         print(div_by_3)
#     elif number % 5 == 0:  # If the number is a multiple of 5
#         print(div_by_5)
#     elif number % 7 == 0:  # If the number is a multiple of 7
#         print(div_by_7)
#     else:
#         print(number)  # If it doesnt satify any of the above cases, we simply print this number



# Start_number = int(input('start value\n'))
# End_number = int(input('End value\n'))
#
# for n in range(Start_number, End_number + 1):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)

# FizzBuzz in the form of a function


def FizzBuzz_game():
    Start_number = int(input('start value\n'))  # User input for start number
    End_number = int(input('End value\n'))  # User input for end number
    div_by_3 = input('How would you want to describe the number if divisible by 3?\n')
    div_by_5 = input('How would you want to describe the number if divisible by 5?\n')
    div_by_3_and_5 = input('How would you want to describe the number if divisible by both 3 and 5?\n')

    for number in range(Start_number, End_number):
        if number % 3 == 0 and number % 5 == 0:
            print(div_by_3_and_5)
        elif number % 3 == 0:
            print(div_by_3)
        elif number % 5 == 0:
            print(div_by_5)
        else:
            print(number)
    return


FizzBuzz_game()
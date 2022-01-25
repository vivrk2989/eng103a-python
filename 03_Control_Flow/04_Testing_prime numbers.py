
Start_number = int(input('start value\n'))  # User input for start number
End_number = int(input('End value\n'))  #User input for end number

prime_number = input('How would you want to describe the number if it is prime?\n')

for num in range(Start_number, End_number + 1):
    if num > 1:  #Prime numbers are greater than 1. 1 is neither prime nor composite
        for p in range(2,num):  #lets say num = 2, then we have range(2,2) which has len 0. lets say num = 5, then the range the for loop here looks at is only till 4. So 5 will not be divisible by anything in that range,
                                # so it breaks and goes to the else line outside the if statement
            if (num % p) == 0:  # will check for all the combinations within the range(2, num)
                break

        else:
            print(f"{num} is a {prime_number}")



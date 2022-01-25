# i = 1
# keep_looping = True
#
# while keep_looping:
#     print(i)
#     if i == 5:
#         print("FIVE PARTY!")
#         keep_looping = False
#     i += 1
#     print("Start again")
#
# print("End of Loop")
#
#
# for x in ['a', 'b', 'c', 'd', 'e']:
#     n = 100
#     while n < 110:
#         print(x, n)
#         if x == 'b' and i == 105:
#             break_for = True
#             break
#         n += 1
#     if break_for:
#         break
#
prompt_user = True
age = None
while prompt_user:
    age = input("What is your age?\n")
    if age.isdigit():
        if int(age) <= 119:
            prompt_user = False
        else:
            print("You are not that old")
    else:
        print("Please provide age in digits")

print(f"Double you age is {int(age) * 2}")

# max age = 119



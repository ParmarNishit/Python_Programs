# def check_even_odd(number):
#     if number - (number // 2 * 2) == 0:
#         return "Even"
#     else:
#         return "Odd"

# number = int(input("Enter a number: "))
# print(check_even_odd(number))

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

number = int(input("Enter a number: "))

if (number & 1 == 0):
    print("Even number")
else:
    print("Odd number")
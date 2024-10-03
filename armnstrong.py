number = int(input("Enter a number: "))
num_str = str(number)
num_digit = len(num_str)

sum_of_power = 0

for digit in num_str:
    sum_of_power = sum_of_power + int(digit) ** num_digit

if sum_of_power == number:
    print("Armstrong number")
else:
    print("Not Armstrong number")
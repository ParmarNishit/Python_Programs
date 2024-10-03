total = 1

number = int(input("Enter number: "))

for i in range(1,number + 1):
    total = i * total
print("Factorial is ",total)
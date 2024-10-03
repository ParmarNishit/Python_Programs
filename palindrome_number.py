number = input("Enter a number: ")

reverse_number = ""

for i in number:
    reverse_number = i + reverse_number

if (reverse_number == number):
    print("Palindrome")
else:
    print("Not Palindrome")
string = input("Enter a string: ")

reverse_str = ""

for i in string:
    reverse_str = i + reverse_str

if (reverse_str == string):
    print("Palindrome")
else:
    print("Not Palindrome")
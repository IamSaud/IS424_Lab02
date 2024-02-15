#Saud AlQahtani
# 442101254

# Program to print the multiplication table of a number entered by the user.

number = int(input("Enter a number: "))

print("Multiplication Table for", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Saud AlQahtani
# 442101254

# Program to find the largest number in a list of 10 numbers.

numbers = []
for i in range(10):
    numbers.append(int(input("Enter a number: ")))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)

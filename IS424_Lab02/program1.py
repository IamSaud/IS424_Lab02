# Saud AlQahtani
# 442101254

# Program to store employee names and salaries in a dictionary.

employee_data = {}

while True:
    name = input("Enter employee name: ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_data[name] = salary

print("Employee data:", employee_data)

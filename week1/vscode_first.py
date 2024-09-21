# print("\033[91mHello, World!\033[0m")

# PI = 3.14
# PI = 3.15

# print(PI)

# name = input("Enter a name: ")
# character_count = len(name)
# print("Number of characters:", character_count)

# Get two numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Perform division and print the result
# if num2 != 0:
#     result = num1 / num2
#     print("Result of division:", result)
# else:
#     print("Error: Division by zero is not allowed.")
    
    
# total_sum = 0.0

# while True:
#     user_input = input("Enter a number (or type 'done' to finish): ")
    
#     if user_input.lower() == 'done':
#         break
    
#     try:
#         number = float(user_input)
#         total_sum += number
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# print("Total sum of entered numbers:", total_sum)

import random

students_grades = {}

while True:
    full_name = input("Enter the student's full name (or type 'done' to finish): ")
    
    if full_name.lower() == 'done':
        break
    
    grade = random.randint(0, 100)
    students_grades[full_name] = grade

print("\nStudent Grades:")
for student, grade in students_grades.items():
    print(f"{student}: {grade}")
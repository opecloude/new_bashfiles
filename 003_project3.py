# 003_project 
# This program will will use conditional statements to test for different conditions
# It will use <, >, <=, >=, != == conditions.

print('Enter two integers and I will tell you',
'the relationships they satisfy.')

num1 = int(input('Enter first integer: '))

num2 = int(input(' Enter second integer: '))

if num1 == num2:
    print(num1, 'is equal to ', num2)

if num1 >= num2:
    print(num1, 'is grearer than or equal to ', num2)

if num2 <= num1:
    print(num2, 'is less than or equal to ', num1)

if num1 != num2:
    print(num1, 'is not equal to ', num2)
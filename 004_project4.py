#004_project_A.py
'''Finds the Minimum of three values'''

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))
num3 = int(input('Enter the third number: '))


mini = num1

if num2 < mini:
    mini = num2

if num3 < mini:
    mini = num3

print('The minimum value is: ', mini)


grade =int(input('\n\nEnter your letter grade: '))
score = grade

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print("Sorry! Check back on ur grade!!!")    


shift_staff = str(input('Enter name of staf working tonight: '))

name = shift_staff

if name != shift_staff:
    print('Thanks for taking up this shift,'
    'at this time')
else:
    print('We can\'\n/t find soneone to cover')

product = 4

while product <= 50:
    product = product * 4

print(product) 

product1 = 7

while product1 <= 1000:
    product1 = product1 * 7

print(product1) 


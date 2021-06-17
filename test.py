name = input("введите слово: ")
last_name = name[:-1]
str_name = " "
for x in range(0, len(last_name)):
if x != 2:
str_name = str_name + last_name[x]
print(str_name)

import math
num1 = int(input("число="))
numf = math.factorial(num1)
print(numf)

import math
import random
#vs - возведение в степень, m - модуль, 0 - рандом, ! - факториал, ac - арккосинус
print('+, -, *, /, vs, m, r, !, ac')
operator1 = input("Введите оператор : ")
number1 = float(input("Введите первое число : "))
if operator1 == 'm':
    print("Результат = ", abs(number1))
elif operator1 == 'r':
    print("Результат = ", random.randом)
elif operator1 == '!':
    while number1<0 and
    print("Результат = ", math.factorial(number1))
number2 = float(input("Введите второе число : "))
if operator1 == '+':
    print("Результат = ", number1 + number2)
elif operator1 == '-':
    print("Результат = ", number1 - number2)
elif operator1 == '*':
    print("Результат = ", number1 * number2)
elif operator1 == '/':
    if number2 == 0:
        print("На 0 делить нельзя!")
    else: print("Результат = ", number1 / number2)
elif operator1 == 'vs':
    print("Результат = ", number1 ** number2)
elif operator1 == '*':
    print("Результат = ", number1 * number2)
#num1 = int(input("число="))
#numf = math.factorial(num1)
#print(numf)
# Блок 1. Задача 1. Заочное. гр. 1022-03. Васьков С.А.
import random
randomNumber = random.randint(0, 100)
print("Введите целое число от 0 до 100 = ")
number = int(input())
print("Случайное число = ", randomNumber)
print("Введенное число = ", number)
if randomNumber < number:
    print("Случайное число меньше")
elif randomNumber > number:
    print("Случайное число больше")
else:
    print("Числа равны")

# Блок 1. Задача 1.
print("Введите число = ")
number = float(input())
print("Введите пограничное число = ")
numberP = float(input())
if number < numberP:
    print("Ваше число меньше пограничного")
elif number > numberP*3:
    print("Ваше число больше пограничного более, чем в 3 раза")
elif number > numberP:
    print("Ваше число больше пограничного")
else:
    print("Числа равны")
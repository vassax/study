# Блок 3. Задача 8. Калькулятор функции в классе
import math
import random


class Calc:

    def plus(self, number1, number2):
        print("Сумма = ", float(number1 + number2))

    def minus(self, number1, number2):
        print("Разность = ", float(number1 - number2))

    def multi(self, number1, number2):
        print("Произведение = ", float(number1 * number2))

    def div(self, number1, number2):
        print("Частное = ", float(number1 / number2))

    def exp(self, number1, number2):
        print(number1, "в степени", number2, "=", float(number1 ** number2))

    def mod(self, number1):
        print("Модуль числа = ", float(abs(number1)))

    def rand(self, number1, number2):
        print("Случайное число = ", random.uniform(number1, number2))

    def fact(self, number1):
        print(number1, "! = ", math.factorial(number1))

    def arc(self, number1):
        print("Арккосинус", number1, "=", math.acos(number1), "рад")


c = Calc()

print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
print('Для выхода наберите exit')
Operator = input("Введите оператор : ")
while Operator != "exit":
    if Operator == "+":
        c.plus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "-":
        c.minus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "*":
        c.multi(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "/":
        c.div(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "^":
        c.exp(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "m":
        c.mod(float(input("Введите число: ")))
    elif Operator == "r":
        c.rand(float(input("Введите верхнюю границу случайного числа: ")),
               float(input("Введите нижнюю границу случайного числа: ")))
    elif Operator == "!":
        c.fact(int(input("Введите целое неотрицательное число: ")))
    elif Operator == "ac":
        c.arc(float(input("Введите число в диапазоне от -1 до 1: ")))
    Operator = input("Введите оператор : ")

# Блок 3. Задача 7. Калькулятор на функциях
import math
import random


def plus(number1, number2):
    print("Сумма = ", float(number1 + number2))


def minus(number1, number2):
    print("Разность = ", float(number1 - number2))


def multi(number1, number2):
    print("Произведение = ", float(number1 * number2))


def div(number1, number2):
    print("Частное = ", float(number1 / number2))


def exp(number1, number2):
    print(number1, "в степени", number2, "=", float(number1 ** number2))


def mod(number1):
    print("Модуль числа = ", float(abs(number1)))


def rand(number1, number2):
    print("Случайное число = ", random.uniform(number1, number2))


def fact(number1):
    print(number1, "! = ", math.factorial(number1))


def arc(number1):
    print("Арккосинус", number1, "=", math.acos(number1), "рад")


print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
print('Для выхода наберите exit')
Operator = input("Введите оператор : ")
while Operator != "exit":
    if Operator == "+":
        plus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "-":
        minus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "*":
        multi(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "/":
        div(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "^":
        exp(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "m":
        mod(float(input("Введите число: ")))
    elif Operator == "r":
        rand(float(input("Введите верхнюю границу случайного числа: ")),
         float(input("Введите нижнюю границу случайного числа: ")))
    elif Operator == "!":
        fact(int(input("Введите целое неотрицательное число: ")))
    elif Operator == "ac":
        arc(float(input("Введите число в диапазоне от -1 до 1: ")))
    Operator = input("Введите оператор : ")
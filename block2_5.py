# Блок 2. Задача 5. Про овощи
vegetable1 = input("Введите название первого овоща: ")
vegetable2 = input("Введите название второго овоща: ")
vegetable3 = input("Введите название третьего овоща: ")
print(vegetable1.lower(), vegetable2.lower(), vegetable3.lower())
print(vegetable1.upper(), vegetable2.upper(), vegetable3.upper())
print(vegetable1.title(), vegetable2.title(), vegetable3.title())
countVegetable1 = input("Введите количество первого овоща: ")
countVegetable2 = input("Введите количество второго овоща: ")
countVegetable3 = input("Введите количество третьего овоща: ")
print('{} - {} кг.'.format(vegetable1.title(), countVegetable1))
print('{} - {} кг.'.format(vegetable2.title(), countVegetable2))
print('{} - {} кг.'.format(vegetable3.title(), countVegetable3))

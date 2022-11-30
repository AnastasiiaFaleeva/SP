# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
from random import randint

amount_list_elements = int(input('Введите количество элементов списка - '))
diapason_start = int(input('Диапазон случайных чисел от - '))
diapason_end = int(input('Диапазон случайных чисел до - '))
list = []
for i in range(amount_list_elements):
    list.append(randint(diapason_start, diapason_end))
print('Список из случайных чисел - ', list)

new_list = []
for i in range(len(list)//2):
        new_list.append(list[i] * list[len(list) - i -1])

if amount_list_elements % 2 != 0:
    new_list.append(list[len(list)//2] * list[len(list)//2])
print(new_list)

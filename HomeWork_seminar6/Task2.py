# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
#
# amount_list_elements = int(input('Введите количество элементов списка - '))
# diapason_start = int(input('Диапазон случайных чисел от - '))
# diapason_end = int(input('Диапазон случайных чисел до - '))
# list = []
#
# for i in range(amount_list_elements):
#     list.append(randint(diapason_start, diapason_end))
# print('Список из случайных чисел - ', list)
#
# count = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         count += list[i]
# print('Сумма элементов на нечетных позициях списка = ', count)

from random import randint

amount_list_elements = int(input('Введите количество элементов списка - '))
diapason_start = int(input('Диапазон случайных чисел от - '))
diapason_end = int(input('Диапазон случайных чисел до - '))
my_list = []

for i in range(amount_list_elements):
    my_list.append(randint(diapason_start, diapason_end))
print('Список из случайных чисел - ', my_list)

def summa(my_list: list) -> int:
    return sum([num for i, num in enumerate(my_list) if i % 2])

print('Сумма элементов на нечетных позициях списка = ', summa(my_list))


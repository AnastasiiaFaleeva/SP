# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
from random import randint

amount_elements = int(input('Введите количество элементов списка - '))
diapason_start = float(input('Диапазон случайных чисел от - '))
diapason_end = float(input('Диапазон случайных чисел до - '))
list = []
for i in range(amount_elements):
    list.append(round(random.uniform(diapason_start, diapason_end), 1))
print('Список из случайных чисел - ', list)

new_list = []
for i in list:
    if (i*10)%10 != 0:
      new_list.append (int(i*10)%10)
print('Список из дробной части элементов - ', new_list)

print('Разница между макс и мин значением дробной части - ', (max(new_list) - min(new_list))/10)






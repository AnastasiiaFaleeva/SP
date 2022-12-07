# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import sympy as sympy

import function_file as ff

# вводим к
k = input('Введите число k: ')
name1 = 'result1'
name2 = 'result2'

# применяем функцию из файла для создания и записи многочлена в файл
ff.polynominal(k, name1)
ff.polynominal(k, name2)

# открываем созданные файлы для чтения
with open(name1, 'r') as data:
    result_1 = data.readline()

with open(name2, 'r') as data:
    result_2 = data.readline()

# удаляем из строки первого файла все, кроме чисел
result_1 = result_1.replace(f'*x**{k}', '')
result_1 = result_1.replace('= 0', '')
result_1 = result_1.replace('+', '')

# преобразуем строку в число
result_1 = int(result_1)

# число в список
count = int(k)
new_list =[]
for i in range(count):
    if result_1 > 1:
     new_list.append(result_1%100)
     result_1 = result_1//100
new_list.reverse()

# повторяем тоже самое для строки из второго файла
count = int(k)
result_2 = result_2.replace(f'*x**{k}', '')
result_2 = result_2.replace('= 0', '')
result_2 = result_2.replace('+', '')
result_2 = int(result_2)
new_list_2 =[]
for i in range(count):
    if result_2 > 1:
     new_list_2.append(result_2%100)
     result_2 = result_2//100
new_list_2.reverse()

# список из суммы элементов двух списков
result_list = []
for i in range(count):
    result_list.append(new_list[i] + new_list_2[i])
    i += 1

result = ''
for i in result_list:
    result += (f'{i}*x**{k}+')
    count -= 1
    i += 1
result = result[:-1]
result += ('= 0')
with open('sum_file', 'w') as file:
     file.write(result)
     file.close()

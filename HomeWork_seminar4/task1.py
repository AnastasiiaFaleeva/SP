# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import random

k = input('Введите число k: ')

def polynominal(k):
 count = int(k)
 result = ''
 temp = []
 for i in range(count):
     temp.append(randint(0, 100))
 for i in temp:
    result += (f'{i}*x**{k} + ')
    count -= 1
    i += 1
 result = result[:-2]
 result += (' = 0')
 print(result)
 with open('task1', 'w') as file:
     file.write(result)
     file.close()

polynominal(k)

# Напишите программу, которая будет преобразовывать десятичное
# число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число - '))

list = []
while num > 0:
          list.insert(0, str(num % 2))
          num = num // 2

print('Двоичное число - ', ''.join(list))
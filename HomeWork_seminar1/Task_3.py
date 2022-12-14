# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

x = int(input('Введите координату х - '))
y = int(input('Введите координату y - '))

if x == 0 or y == 0:
    print('Введены некорретные значения одной или нескольких координат')
elif x > 0 and y > 0:
    print(f'Значения х = {x} и у = {y} являются координатами 1 четверти')
elif x < 0 and y > 0:
    print(f'Значения х = {x} и у = {y} являются координатами 2 четверти')
elif x < 0 and y < 0:
    print(f'Значения х = {x} и у = {y} являются координатами 3 четверти')
else:
    print(f'Значения х = {x} и у = {y} являются координатами 4 четверти ')

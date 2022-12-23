# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# import math
#
# xA = int(input('Введите координату х точки А '))
# yA = int(input('Введите координату y точки А '))
# xB = int(input('Введите координату х точки B '))
# yB = int(input('Введите координату y точки B '))
#
# distans2D = math.sqrt(((xB - xA) ** 2) + ((yB - yA) ** 2))
# print('Расстояние между точками А и В =  ', round(distans2D, 3))

from functools import reduce
point_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split()))
point_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def distans2D(dot_1, dot_2):
     dis = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(dis, 2)
print(distans2D(point_1, point_2))
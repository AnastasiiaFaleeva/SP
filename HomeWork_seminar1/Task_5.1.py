# Нахождение координат в 3D пространвтсве
import math

x_A = int(input('Введите координату х точки А '))
y_A = int(input('Введите координату y точки А '))
z_A = int(input('Введите координату z точки А '))
x_B = int(input('Введите координату х точки B '))
y_B = int(input('Введите координату y точки B '))
z_B = int(input('Введите координату z точки B '))


distans3D = math.sqrt(((x_B - x_A) ** 2) + ((y_B - y_A) ** 2) + ((z_B - z_A) ** 2))
print('Расстояние между точками А и В в пространстве =', round(distans3D, 3))

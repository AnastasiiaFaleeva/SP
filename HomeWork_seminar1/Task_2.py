# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input('Введите значение первого предиката, где 1 - истина, 0 - ложь - '))
y = int(input('Введите значение второго предиката, где 1 - истина, 0 - ложь - '))
z = int(input('Введите значение второго предиката, где 1 - истина, 0 - ложь - '))

if (not (x or y or z)) == (not x) and (not y) and (not z):
      print('Утверждение истинно')
else:
      print('Утверждение ложно')


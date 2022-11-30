# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число - ')


def SumNumbers(number):
    number = number.replace('.', '')
    number = number.replace(',', '')
    summa = 0
    for i in number:
        summa = summa + int(i)
    return summa


print('Сумма цифр в числе', num, '=', SumNumbers(num))

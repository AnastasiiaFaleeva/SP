# Напишите программу, которая
# по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

quarter_num = int(input('Введите номер четверти '))

if quarter_num == 1:
    print('Диапазон значений координат х > 0 и у > 0')
elif quarter_num == 2:
    print('Диапазон значений координат х < 0 и у > 0')
elif quarter_num == 3:
    print('Диапазон значений координат х < 0 и у < 0')
elif quarter_num == 4:
    print('Диапазон значений координат х > 0 и у < 0')
else:
    print('Введен неверный номер четверти')

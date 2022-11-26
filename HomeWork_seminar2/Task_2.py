# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.


n = int(input('Введите количество элементов списка '))

def Spisok(n):
    list = []
    for i in range(1, n + 1):
        list.append((1 + 1/i) ** i)
    return list

def Sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

list = Spisok(n)
print(list)
print(Sum(list))
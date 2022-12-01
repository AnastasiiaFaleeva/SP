# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input())

list = [0, 1]
for i in range(n - 1):
       list.append(list[i] + list[i + 1])

list_2 = []
for i in range(n):
        if i% 2 == 0:
             list_2.insert(0, list[i+1])
        else:
            list_2.insert(0, list[i+1]*(-1))

negafibonachi_list = list_2 + list
print(negafibonachi_list)



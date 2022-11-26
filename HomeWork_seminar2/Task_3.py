# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
from random import randint

list = []
for i in range(0,10):
    list.append(i+1)
print(list)

def shuf(list):
    for i in range(len(list)):
        random_num = randint(1, 11)
        temp = list[i]
        list[i] = list[random_num]
        list[random_num] = temp
    return list

print(shuf(list))
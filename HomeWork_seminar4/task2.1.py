from random import randint

k = input('Введите число натуральной степени к: ')

temp_1 = []
count = int(k)

for i in range(count):
    temp_1.append(randint(0, 100))

result_1 = ''
for i in temp_1:
    result_1 += (f'{i}*x**{k} + ')
    count -= 1
    i += 1
result_1 = result_1[:-2]
result_1 += (' = 0')
with open('file1', 'w') as file:
    file.write(result_1)
    file.close()

temp_2 = []
count2 = int(k)
for i in range(count2):
    temp_2.append(randint(0, 100))

result_2 = ''
for i in temp_2:
    result_2 += (f'{i}*x**{k} + ')
    count2 -= 1
    i += 1
result_2 = result_2[:-2]
result_2 += (' = 0')
with open('file2', 'w') as file:
    file.write(result_2)
    file.close()

result_temp = []
for i in range(len(temp_1)):
    result_temp.append(int(temp_1[i]) + int(temp_2[i]))
    i += 1

result_3 = ''
for i in result_temp:
    result_3 += (f'{i}*x**{k} + ')
    count -= 1
    i += 1
result_3 = result_1[:-2]
result_3 += (' = 0')
with open('result_file', 'w') as file:
    file.write(result_3)
    file.close()

print(result_1)
print(result_2)
print(result_3)
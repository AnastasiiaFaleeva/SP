
import random

def polynominal(k, name):
 count = int(k)
 result = ''
 temp = []
 for i in range(count):
     temp.append(random.randint(10, 100))
 for i in temp:
    result += (f'{i}*x**{k}+')
    count -= 1
    i += 1
 result = result[:-1]
 result += ('= 0')
 with open(name, 'w') as file:
     file.write(result)
     file.close()
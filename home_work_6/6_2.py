# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

my_list = [randint(0,10) for i in range(20)]
print(f"Список: {my_list}")

ot = 1
do = 4
print(f"Диапазон значений от {ot} до {do}")

diapason = [i for i in range(ot, do)]
print(diapason)

indexes = []

for i in range(len(my_list)):
    if my_list[i] in diapason:
        indexes.append(i)

print(f"Индексы значений нашего диапазона: {indexes}")
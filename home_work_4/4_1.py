# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Введите кол-во эл. 1-ого мн-ва:_ "))
m = int(input("Введите кол-во эл. 2-ого мн-ва:_ "))

list1 = []
list2 = []

for i in range(n):
    list1.append(int(input("1-е мн-во, введите число:_")))

for i in range(m):
    list2.append(int(input("2-е мн-во, введите число:_")))


# list1 = [randint(1,10) for i in range(n)]
# list2 = [randint(1,10) for i in range(m)]
print(f"{list1},\n{list2}")

set1 = set(list1)
set2 = set(list2)

cross_set = set1.intersection(set2)
if not cross_set:
    print("Нет пересечений.")
else:
    mlist = list(cross_set)
    mlist.sort()
    print(mlist)
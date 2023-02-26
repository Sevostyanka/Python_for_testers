# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = 10
x = 5
mlist = [randint(1,50) for i in range(n)]
mlist.append(5)
# mlist = [5 for i in range(n)]
print(mlist)
print(f"Ищем ближайшие к '{x}'")
max = 0
min = 0
dif_max = 1000
dif_min = 1000
for i in range(len(mlist)):
    if 0 < mlist[i]-x < dif_max and mlist[i]!=x:
        dif_max = mlist[i]-x
        max = mlist[i]
    elif 0 < x - mlist[i] < dif_min and mlist[i] != x:
        dif_min = x - mlist[i]
        min = mlist[i]
if dif_min == 1000:
    print(f"Число меньше '{x}' отсутствует")
    print(f"Ближайшее большее - '{max}', больше на {dif_max}")
elif dif_max == 1000:
    print(f"Число больше '{x}' отсутствует")
    print(f"Ближайшее меньшее - '{min}', меньше на {dif_min}")
elif dif_min == 1000 and dif_max == 1000:
    print(f'Верь ряд состоит из числа "{x}"')
else:
    print(f"Ближайшее меньшее - '{min}', меньше на {dif_min}")
    print(f"Ближайшее большее - '{max}', больше на {dif_max}")

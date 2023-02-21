# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
n = 20
all_money = []
for i in range(n):
    all_money.append(randint(0,1))
print(all_money)

count_zero = 0
count_one = 0

if 0 in all_money:
    count_zero = all_money.count(0)

if 1 in all_money:
    count_one = all_money.count(1)
    print(f"Решкой(1) -> {count_one}, орлом(0) -> {count_zero}")

if count_one <= count_zero:
    for i in range(len(all_money)):
        if all_money[i] == 1:
            all_money[i] = 0
else:
    for i in range(len(all_money)):
        if all_money[i] == 0:
            all_money[i] = 1
print(all_money)
# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = input("Введите число: ")
a = list(a)
a = list(map(int, a))
sum = 0
for i in range(len(a)):
    sum+=a[i]

print(sum)
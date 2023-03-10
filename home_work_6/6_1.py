# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой

# first = int(input())
# step = int(input())
# dlina = int(input())

first = 3
step = 2
dlina = 6
print(f"ЗАДАНО: старт = {first}, шаг = {step}, длина = {dlina}\nПолучилось:")
i = 1
a = [first]
current = first

while i < dlina:
    current += step
    a.append(current)
    i+=1
    
print(a)
    
# Напишите функцию | print_operation_table(operation, num_rows=6, num_columns=6) |,
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

operation1 = lambda x, y: x * y

def print_operation_table(operation, num_rows, num_col):
    list1 = list(range(1,num_col+1)) #задала список
    print(list1)
    print()
    
    for i in range(1, num_rows):
        row = [i+1]
        for j in range(0, num_rows-1):
            row.append(row[j]+i+1)
        print(row)
        
print_operation_table(operation1, 6, 6)

    
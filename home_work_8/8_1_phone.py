# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефна - данные, которые должны находиться в файле
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определённой записи 
# (Например, имя или фамилию человека)
# 4. Использование ф-ций. Ваша программа ге должна быть линейной.

import func

def switcher(a):
    match a:
        case 1:
            func.print_base(func.data) # открыть файл и считать базу  
        case 2:
            func.data
            func.find_by_surname()             
        case 3:
            func.data
            func.find_by_number()
        case 4:
            func.add_person() 
        case 5:
            func.save_base()
        case 6:
            exit

while True:
    func.show_menu()
    if switcher(func.user_choise()) == 6:
        False
    
    


  
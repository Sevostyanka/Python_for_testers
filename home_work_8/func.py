def user_choise():
    num = int(input("Введите цифру:_"))
    print("\n")
    return num

path = "phone.txt"

def base(fileName):
    data = []
    fields = ('Фамилия', 'Имя', 'Телефон', 'Описание')
    with open (fileName, 'r', encoding='utf-8') as fin:
        for line in fin:
            if line != 0:
                record = dict(zip(fields, line.strip().split(',')))
                data.append(record)   
    return data

data = base(path)

def print_base(list):
    for i in range(len(list)):
        print(f"{i+1}. {list[i]}")
        
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразите весь справочник+.\n"
          "2. Найти абонента по фамилии+.\n"
          "3. Найти абонента по номеру телефона+\n"
          "4. Добавить абонента в справочник+\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу"
          "\n")

def find_by_surname():
    s_name = input("Введите фамилию:_")
    global data
    check = 0
    for i in data:
        if s_name in i.values():
            check += 1
            print(i)
    if check == 0:
        print("Такая фамилия отсутствует в справочнике.")

def find_by_number():
    global data
    s_name = input("Введите номер телефона:_")
    check = 0
    for i in data:
        if s_name in i.values():
            check += 1
            print(i)
    if check == 0:
        print("Такой номер отсутствует в справочнике.")
            
def add_person():
    global data
    fields = ('Фамилия', 'Имя', 'Телефон', 'Описание')
    person = []
    surname = input("Введите фамилию:_")
    name = input("Введите имя:_")
    phone = input("Введите номер телефона:_")
    about = input("Введите описание:_")
    person.append(surname)
    person.append(name)
    person.append(phone)
    person.append(about)
    new_line = dict(zip(fields, person))
    person_line = ""
    
    for v in new_line.values():
        person_line = person_line + v + ","
    person_line = person_line[:-1] + "\n"
    
    global path
    
    with open (path, "a", encoding="UTF-8") as file:
        file.writelines(person_line)
    print("Профиль добавлен")
    
def save_base(): #так получилось, что сохранение в файл я прописала выше, в ф-ции добавления профиля.
    global data
    data = base(path)
    print("Данные сохранены в файл")
    
    

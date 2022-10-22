def create_card():
    with open('base.csv', 'a', encoding='utf-8') as file:
        file.write('{card_list}\n')


import csv


# Получаем карточку в виде списка, функция считывает значение первого индекса последней строки (id), увеличивает его на
# единицу и добавляет в список

# Пример передаваемых в виде списка данных, которые добавляются в list, при вводе пользователем, например list.append()

card = ['Иванов', 'Иван', 'Иванович', '89060000000', '20.05.2020', 'слесарь']


def write_to_csv(anylist):
    with open('db.csv', 'r', encoding='utf8', newline='') as myfile:
        rd = myfile.readlines()
        ident = 0
        if rd: ident = rd[-1][0]
        anylist.insert(0, int(ident)+1)
    with open('db.csv', 'a', encoding='utf8', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(anylist)


write_to_csv(card)


def check_name(name):
    while not name.isalpha():
        print("""Error! 
         Можно вводить русские 
         или латинские буквы!""")
        name = input("Попоробуйте снова: ")
    name = name.lower()
    name = name.capitalize()
    return name

def check_name(name):
    while not name.isalpha():
        print("""Error! 
         Можно вводить русские 
         или латинские буквы!""")
        name = input("Попоробуйте снова: ")
    name = name.lower()
    name = name.capitalize()
    return name

def check_phone(phone):
    while not (phone.isdigit() and 4<len(phone)<16):
        print(""" 
        Можно вводить только цифры
        в количестве от 5 до 15""")
        phone = input("Введите номер телефона: ")
    return phone

def check_comment(name):
    if len(name)>255:
        print('''Количество символов 
        не должно быть более 40''')
        name = input("Пожалуйста, введите корректные значения: ")
    return name

def menu_changes():
    menu = """-'*50\n
    Выберите значения, которое которое нужно изменить.
    для изменения фамилии нажмите:                  1
    для изменения имени нажмите:                    2
    для изменения отчества:                         3
    для изменения номера телефона:                  4
    для изменения должности:                        5
    для выхода:                 любую цифру или букву
    
    """
    choice = input(menu)
    if choice not in ['1','2','3','4','5']:
        exit()
    else:
        return choice

def preparing_for_change():
    query = input("Для изменения карточки сотрудника введите его фамилию: ")
    query = check_name(query)
    list_for_changes = []
    with open(r'.\db.csv', 'r', encoding='utf-8') as my_file:
        rd = my_file.readline()
        temp = []   
        for row in rd:
            temp.append([row])
        for i in temp:
            if query in i:
                list_for_changes.append(i)
    if len(list_for_changes) == 0:
        print("Такого сотрудника не найдено")
        exit()
    else:
        for line in list_for_changes:
            print(line)
            print()
    user_id = input('Введите id записи: ')
    answer = menu_changes()
    if answer == '1':
        new_last_name = input("Введите новую фамилию: ")
        new_last_name = check_name(new_last_name)
        update(id=user_id, new_last_name =new_last_name)
    elif answer == '2':
        new_first_name = input("Введите новое имя: ")
        new_first_name = check_name(new_first_name)
        update(id=user_id, new_last_name =new_first_name)
    elif answer == '3':
        new_patronimyc = input("Введите новое отчество: ")
        new_patronimyc = check_name(new_patronimyc)
        update(id=user_id, new_patronimyc = new_patronimyc)
    elif answer == '4':
        new_phone = input("Введите номер телефона: ")
        new_phone = check_phone(new_phone)
        update(id=user_id, new_phone = new_phone)
    elif answer == '5':
        new_post = input("Введите новую должность:")
        new_post = check_comment(new_post)
        update(id=user_id, new_post = new_post)
    
def update(id, new_last_name = '', new_first_name = '', new_patronymic = '', new_phone = '', new_post = ''):
    with open(r'db.csv', 'r', newline='') as my_file:
        wr = csv.reader(my_file)
        temp = []
        for row in wr:
            temp.append(row)              
            if (temp[-1][0] == id):
                anylist = temp.pop()
                if(new_last_name != ''):
                    del anylist[1]
                    anylist.insert(1, new_last_name)
                if(new_first_name != ''):
                    del anylist[2]
                    anylist.insert(2, new_first_name)
                if(new_patronymic != ''):
                    del anylist[3]
                    anylist.indert(3, new_patronymic)
                if(new_phone != ''):
                    del anylist[4]
                    anylist.insert(4, new_phone)  
                if(new_post != ''):
                    del anylist[5]
                    anylist.insert(5, new_post)
                temp.append(anylist)
    with open(r'base.csv') as file:
            writer = csv.writer(file)
            writer.writerows(temp)

preparing_for_change()
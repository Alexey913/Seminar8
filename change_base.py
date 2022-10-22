def create_card():
    with open('base.csv', 'a', encoding='utf-8') as file:
        file.write('{card_list}\n')


import csv


# Получаем карточку в виде списка, функция считывает значение первого индекса последней строки (id), увеличивает его на
# единицу и добавляет в список

# Пример передаваемых в виде списка данных, которые добавляются в list, при вводе пользователем, например list.append()

card = ['Иванов', 'Иван', 'Иванович', '89060000000', '20.05.2020', 'слесарь']

from log import *
def write_to_csv(anylist):
    with open('db.csv', 'r', encoding='utf8', newline='') as myfile:
        rd = myfile.readlines()
        ident = 0
        if rd: ident = rd[-1][0]
        anylist.insert(0, int(ident)+1)
    with open('db.csv', 'a', encoding='utf8', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(anylist)

    logger.debug('change_base.py/write_to_csv')

write_to_csv(card)

import csv
from log import *
 
def read_data():
    with open('directory.csv', 'r', encoding="utf-8") as file:  
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
        file.close()

    logger.debug('read_base.py / read_data')

read_data()
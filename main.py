import pickle
import sys
import re

def main():
    # Главный опросник пользователя
    # Список команд: 1 - Вывести все позиции
    # 2 - Добавить позицию
    # 3 - Удалить позицию
    # 4 - Редактировать позицию
    print("Введите номер операции, которую хотите выполнить:")
    print("1. Вывести все позиции товаров на складе ")
    print("2. Добавить новую позицию на складе ")
    print("3. Удалить позицию на складе ")
    print("4. Редактировать позицию на складе ")
    print("5. Закрыть ")
    number_operation = input()
    if number_operation == "5":
        print("Система управления складом закрыта")
        sys.exit()
    elif number_operation == "1":
        select_all_position()
    elif number_operation == '2':
        add_position()
    elif number_operation == '3':
        number = input('Введите номер позиции, которую требуется удалить - ')
        delete_position(number)
    elif number_operation == '4':
        number = input('Введите номер позиции, которую требуется редактировать - ')
        edit_position(number)

def select_all_position():
    data = load_from_file()
    for i in range(len(data)):
        print('Номер - ' + data[i][0] + '; Название - ' + data[i][1] + '; Цена - ' + data[i][2] + '; Номер рейки - ' +
              data[i][3] +
              '; Номер ячейки - ' + data[i][4])


def add_position():
    number = input('Введите номер позиции - ')
    name = input('Введите наименование позиции - ')
    price = input('Введите цену -')
    number_rack = input('Введите номер рейки -')
    number_cell = input('Введите номер ячейки -')
    if number and name and price and number_cell and number_rack:
        add_file(number, name, price, number_rack, number_cell)
    else:
        print('Данные заполнены не полностью')


def delete_position(number_position):
    with open('data.txt') as f:
        lines = f.readlines()
    pattern = re.compile(re.escape(number_position))
    with open('data.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            else:
                print('Позиция с номером ' + number_position + ' удалена')


def edit_position(number_position):
    with open('data.txt') as f:
        lines = f.readlines()
    pattern = re.compile(re.escape(number_position))
    with open('data.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            else:
                temp_var = line.split()
                new_line = []
                print('Номер - ' + temp_var[0])
                new_line.append(input('Новые номер - '))
                print('Название - ' + temp_var[0])
                new_line.append(input('Новое название - '))
                print('Цена - ' + temp_var[0])
                new_line.append(input('Цена - '))
                print('Номер рейки - ' + temp_var[0])
                new_line.append(input('Новый номер рейки - '))
                print('Номер ячейки- ' + temp_var[0])
                new_line.append(input('Новый номер ячейки - '))
                new_line = str(new_line[0] + ' ' + new_line[1] + ' ' + new_line[2] + ' '
                               + new_line[3] + ' ' + new_line[4])
                f.write(new_line)



# функция для записи данных в файл
def add_file(number, name, price, number_rack, number_cell):
    data = number + ' ' + name + ' ' + price + ' ' + number_rack + ' ' + number_cell
    with open("data.txt", "a") as file:
        file.write(data + '\n')
        print('Новые данные записаны')


# функция для ивзлечения данных из файла
def load_from_file():
    data = []
    with open("data.txt", "r") as file:
        line = file.readline()
        while line:
            data_temp_line = line.split()
            data.append(data_temp_line)
            line = file.readline()
    return data


if __name__ == '__main__':
    while True:
        main()

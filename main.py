import pickle


def main():
    # Главный опросник пользователя
    # Список команд: 1 - Вывести все позиции
    # 2 - Добавить позицию
    # 3 - Удалить позицию
    # 4 - Редактировать позицию
    pass


def select_all_position():
    pass


def add_position():
    pass


def delete_position(number_position):
    pass


def edit_position(number_position):
    pass


# функция для записи данных в файл
def add_file(number, name, price, number_rack, number_cell):
    data = number + ' ' + name + ' ' + price + ' ' + number_rack + ' ' + number_cell
    with open ("data.txt", "a") as file:
        file.write(data + '\n')


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
    main()
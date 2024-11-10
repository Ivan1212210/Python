# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    f_i = open(INPUT_FILENAME)
    f_o = open(OUTPUT_FILENAME, 'w')
    read = csv.DictReader(f_i)
    list_ = [i for i in read]
    # TODO Сериализовать в файл с отступами равными 4
    json.dump(list_, f_o, indent=4)
    f_i.close()
    f_o.close()


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

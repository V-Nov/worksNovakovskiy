# TODO импортировать необходимые молули
import csv
import json


input_f = "input.csv"
output_f = "output.json"


def task(input_f, output_f) -> None:

    my_data = []

    with open(input_f) as csv_file:         # TODO считать содержимое csv файла
        csv_read = csv.DictReader(csv_file)

        for row in csv_read:
            my_data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(output_f, "w") as json_file:
        json_string = json.dumps(my_data, indent=4)
        json_file.write(json_string)


if __name__ == '__main__':
    # Нужно для проверки
    task(input_f, output_f)

    with open(output_f) as output_:
        for line in output_:
            print(line, end="")

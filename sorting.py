import os
import csv


# noinspection PyTypeChecker
def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key in row:
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))

    return data


def selection_sort(numbers_list, direction=True):  # direction = "True" (vzestupně), False (sestupně)
    if direction:
        for i in range(1, len(numbers_list)):
            for j in range(len(numbers_list) - 1):
                if numbers_list[j] > numbers_list[i]:
                    numbers_list[j], numbers_list[i] = numbers_list[i], numbers_list[j]
    else:
        for i in range(1, len(numbers_list)):
            for j in range(len(numbers_list) - 1):
                if numbers_list[j] < numbers_list[i]:
                    numbers_list[j], numbers_list[i] = numbers_list[i], numbers_list[j]

    return numbers_list


def bubble_sort(numbers_list):
    for i in range(len(numbers_list) - 1):
        for j in range(len(numbers_list) - 1):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    return numbers_list


def main():
    numbers = read_data("numbers.csv")
    print(selection_sort(numbers["series_1"]))
    print(bubble_sort(numbers["series_1"]))


if __name__ == '__main__':
    main()

import os
import csv


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


def main():
    numbers = read_data("numbers.csv")


if __name__ == '__main__':
    main()

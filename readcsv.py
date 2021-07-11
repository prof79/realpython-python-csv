#!/usr/bin/env python3
# readcsv.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if len(row) == 3:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} works in the {row[1]} department, '
                          f'and was born in {row[2]}.')
                    line_count += 1

        print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

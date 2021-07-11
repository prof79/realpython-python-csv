#!/usr/bin/env python3
# readcsvdict.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

            print(f'\t{row["name"]} works in the {row["department"]}'
                  f' department, and was born in '
                  f'{row["birthday month"]}.')

            line_count += 1

        print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

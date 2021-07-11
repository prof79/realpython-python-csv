#!/usr/bin/env python3
# readcsvaddr3.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_addresses3.txt', mode='r') as csv_file:
        # Use a special escape char (none by default)
        csv_reader = csv.DictReader(csv_file, escapechar='\\')

        for row in csv_reader:
            print(f'{row["name"]} resides at {row["address"]} '
                  f'and joined {row["date joined"]}.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

#!/usr/bin/env python3
# readcsvaddr1.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_addresses1.txt', mode='r') as csv_file:
        # Use a different delimiter
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            print(f'{row["name"]} resides at {row["address"]} '
                  f'and joined {row["date joined"]}.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

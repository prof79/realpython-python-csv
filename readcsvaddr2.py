#!/usr/bin/env python3
# readcsvaddr2.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_addresses2.txt', mode='r') as csv_file:
        # Data is quoted, nothing to do
        # (double quotes are default, quotechar= otherwise)
        csv_reader = csv.DictReader(csv_file,)

        for row in csv_reader:
            print(f'{row["name"]} resides at {row["address"]} '
                  f'and joined {row["date joined"]}.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

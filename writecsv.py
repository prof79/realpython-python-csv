#!/usr/bin/env python3
# writecsv.py
# https://realpython.com/python-csv

import csv


def main() -> None:
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow([
            'John Smith',
            'Accounting',
            'November'
        ])

        employee_writer.writerow([
            'Erica Meyers',
            'IT',
            'March'
        ])

        print('Data written.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

#!/usr/bin/env python3
# writecsvdict.py
# https://realpython.com/python-csv

import csv


FILENAME = 'employee_file2.csv'


def main() -> None:
    with open(FILENAME, mode='w') as employee_file:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        employee_writer = csv.DictWriter(
            employee_file,
            fieldnames=fieldnames
        )

        employee_writer.writeheader()

        employee_writer.writerow({
            'emp_name': 'John Smith',
            'dept': 'Accounting',
            'birth_month': 'November'
        })

        employee_writer.writerow({
            'emp_name': 'Erica Meyers',
            'dept': 'IT',
            'birth_month': 'March'
        })

        print(f'Data written to {FILENAME}.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

#!/usr/bin/env python3
# pandaswritecsv.py
# https://realpython.com/python-csv

import pandas


FILENAME = 'hrdata2.csv'
OUTPUT_FILENAME = 'hrdata_modified.csv'


def main() -> None:
    print('Re-writing CSV ...')
    print()

    # Load a CSV file without header information
    fieldnames = ['Employee', 'Hired', 'Salary', 'Sick Days']

    df = pandas.read_csv(
        FILENAME,
        header=0,
        names=fieldnames,
        index_col=fieldnames[0],
        parse_dates=[fieldnames[1]]
    )

    df.to_csv(OUTPUT_FILENAME)

    print(f'New CSV written to {OUTPUT_FILENAME}.')


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

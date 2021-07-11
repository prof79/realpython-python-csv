#!/usr/bin/env python3
# pandasreadcsv.py
# https://realpython.com/python-csv

import pandas


FILENAME = 'hrdata.csv'
FILENAME2 = 'hrdata2.csv'


def main() -> None:
    print('File #1')
    print()

    # df = pandas.read_csv(FILENAME)
    # Make sure, the index column is the 'Name' column
    # Use date type for the 'Hire Date' column
    df = pandas.read_csv(
            FILENAME,
            index_col='Name',
            parse_dates=['Hire Date'])

    print(df)
    print()
    print()

    print('File #2')
    print()

    # Load a CSV file without header information
    fieldnames = ['Employee', 'Hired', 'Salary', 'Sick Days']

    df2 = pandas.read_csv(
        FILENAME2,
        header=0,
        names=fieldnames,
        index_col=fieldnames[0],
        parse_dates=[fieldnames[1]]
    )

    print(df2)


if __name__ == '__main__':
    print()
    print()
    main()
    print()
    print()

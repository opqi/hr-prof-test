#!/usr/bin/env python

import csv
import codecs
import os


def convert_csv_to_utf8(input_path, output_path):
    # Read the CSV file
    with open(input_path, 'r', encoding='windows-1251') as infile:
        data = csv.reader(infile)
        rows = list(data)

    # Write the contents into another CSV file with UTF-8 encoding
    with codecs.open(output_path, 'w', encoding='utf-8', errors='ignore') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)


def main():
    # Call the convert_csv_to_utf8 function to convert the input CSV
    input_csv = './data/test_data.csv'
    utf8_csv = './data/test_data_utf8.csv'
    convert_csv_to_utf8(input_csv, utf8_csv)

    output_file = './data/test_data_clean.csv'

    with open(utf8_csv, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output, quoting=csv.QUOTE_NONE, escapechar=' ')

        for row in reader:
            # Remove extra quotes using replace()
            modified_row = [value.replace('"', '') for value in row]
            writer.writerow(modified_row)

    try:
        os.remove(utf8_csv)
        print(f'Temporary file {utf8_csv} deleted successfully.')
    except OSError as e:
        print(f'Error deleting file: {e}')


if __name__ == '__main__':
    main()

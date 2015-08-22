import csv
import re
import sys

delimiter = "\" ********************************************************************************\""


def process_row(row):
    row = row.strip()
    fields = re.split(r'\'\'|,|\n', row)
    fields = map(lambda x: x.strip('"'), fields)
    return fields

"""
    sql_text: input SQL dump in text format
    returns list of lists to be written to CSV file.
"""
def convert(sql_text):
    rows = sql_text.split(delimiter)
    rows = map(str.strip, rows)
    headers = []
    row_list = []


    # Add the headers
    fields = process_row(rows[0])
    for field in fields:
        if field.endswith(":"):
            headers.append(field[:-1])
    row_list.append(headers)
    
    # Add each row
    for row in rows:
        fields = process_row(row)
        out_row = []
        for i, field in enumerate(fields):
            if field.endswith(":"):
                out_row.append(fields[i + 1])
        row_list.append(out_row)

    return row_list

def write_csv(rows, output_file_name):
    f = open(output_file_name, 'wt')
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
    f.close()


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    sql_text = open(input_file_name).read().strip()
    rows = convert(sql_text)
    write_csv(rows, output_file_name)



# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=False):
    '''Parse a CSV file into a list of records'''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []

        for row in rows:
            if not row: #skip rows with no data
                continue
            if indices:
                row = [ row[index] for index in indices ]
            if types:
                row = [f(entry) for f,entry in zip(types, row)]
            
            record = dict(zip(headers, row))
            records.append(record)
        
    return records

# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''Parse a CSV file into a list of records'''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if exist)
        if has_headers:
            headers = next(rows)
        
        # If specific columns selected, get their indices to filter
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []

        for row in rows:
            if not row: #skip rows with no data
                continue
                
            # if specific columns have been selected, pick them via indices
            if indices:
                row = [ row[index] for index in indices ]
            
            # apply type conversion to row if provided
            if types:
                row = [f(entry) for f,entry in zip(types, row)]

            # Make dict or tuple 
            if has_headers: 
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        
    return records

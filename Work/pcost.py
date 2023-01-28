# pcost.py
#
# Exercise 1.27
# Exercise 1.30 : Turn code of 1.27 into a funcion
#Exercise 1.32 to use csv lib 
import sys
import csv
def portfolio_cost(filename):
    total = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows) #skip the header

        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += (nshares * price)
            except ValueError:
                print(f'Row {rowno}: Bad row {row}')

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    raise RuntimeError("Missing Filename")

total = portfolio_cost(filename)
print(f'Total Cost {total}')


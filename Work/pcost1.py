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

        try:
            for row in rows:
                nshares = int(row[1])
                price = float(row[2])
                total += (nshares * price)
        except ValueError:
            print('Could not parse row', row)
             
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    raise RuntimeError("Missing Filename")

total = portfolio_cost(filename)
print(f'Total Cost {total}')


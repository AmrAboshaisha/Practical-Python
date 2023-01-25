# pcost.py
#
# Exercise 1.27
total = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f) #skip the header
    
    for line in f:
        stock = line.split(',')
        nshares = int(stock[1])
        price = float(stock[2])
        total += (nshares * price)

print(f'Total Cost {total}')
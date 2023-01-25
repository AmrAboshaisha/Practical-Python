# pcost.py
#
# Exercise 1.27
# Exercise 1.30 : Turn code of 1.27 into a funcion
def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f) #skip the header
        
        try:
            for line in f:
                stock = line.split(',')
                nshares = int(stock[1])
                price = float(stock[2])
                total += (nshares * price)
        except ValueError:
            print('Could not parse line', line)
             
    return total

#total = portfolio_cost('Data/portfolio.csv')
#print(f'Total Cost {total}')

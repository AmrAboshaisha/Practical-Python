# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    '''Reads a portfolio csv file of Stock, Num Shares, Price 
    into a list of dictionaries'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0],'shares':int(row[1]),
            'price':float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    ''' Reads a set of prices into a dictionary where keys are
    the stock names and values are the stock prices'''
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                #print('Could not process', row)
                pass
    return prices

prices = read_prices('Data/prices.csv')
#pprint(prices)

# Calculate total cost of portfolio
def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0
    for s in portfolio:
        total += s['shares']*s['price']
    return total



# Compute current value
def portfolio_value(filename):
    portfolio = read_portfolio(filename)
    total = 0.0
    for s in portfolio:
        total += s['shares'] * prices[s['name']]
    return total

filename = 'Data/portfolio.csv'
current_value = portfolio_value(filename)
total_cost = portfolio_cost(filename)

print('Current Value', current_value)
print('Gain', current_value - total_cost)


portfolio = read_portfolio(filename)
prices = read_prices('Data/prices.csv')

def make_report(protfolio, prices):
    ''' takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples Name, Shares, Price, Change'''
    table = []
    #calculate chage for each stock
    for stock in portfolio:
        if stock['name'] in prices:
            change = prices[stock['name']] - stock['price']
        else:
            change = 0
        record = (stock['name'], stock['shares'], stock['price'], change)
        table.append(record)
    return table

#pprint(make_report(portfolio, prices))

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' %headers)
print(('_' * 10 + ' ')*len(headers))
report = make_report(portfolio, prices)
for record in report:
    print('%10s %10d %10.2f %10.2f' % record)


#for name, shares, price, change in report:
    #print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



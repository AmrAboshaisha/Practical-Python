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
            record = dict(zip(headers, row))
            holding = {
            'name':record['name'],
            'shares':int(record['shares']),
            'price':float(record['price'])
            }
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
                pass
    return prices


def portfolio_cost(filename):
    '''Calculate total cost of portfolio'''
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


def make_report(portfolio, prices):
    ''' takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples Name, Shares, Price, Change'''
    table = []
    #calculate chage for each stock
    for stock in portfolio:
        current_price = prices[stock['name']]
        if stock['name'] in prices:
            change = current_price - stock['price']
        else:
            change = 0
        record = (stock['name'], stock['shares'], current_price, change)
        table.append(record)
    return table

def print_report(report):
    '''Prints a nicely formatted table'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    print(('_' * 10 + ' ')*len(headers))
    for record in report:
        print('%10s %10d %10.2f %10.2f' % record)


def portfolio_report(portfolio_filename, prices_filename):
    ''' Make a stock report given portfolio and price data files'''
    
    # read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # create report data
    report = make_report(portfolio, prices)

    # print it out    
    print_report(report)


portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')


files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()
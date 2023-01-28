#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
from fileparse import parse_csv

def file2iter(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line)
    return lines

def read_portfolio(filename):
    '''Reads a portfolio csv file of Stock, Num Shares, Price 
    into a list of dictionaries'''
    return parse_csv(file2iter(filename),select=['name','shares','price'], types=[str,int,float] )


def read_prices(filename):
    ''' Reads a set of prices into a dictionary where keys are
    the stock names and values are the stock prices'''
    return dict(parse_csv(file2iter(filename), has_headers=False, types=[str,float]))


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


def main(argv):
    ''' 
    Accepts a list of command line options to produce the output.
    Example use:
    >>> report.main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
    '''
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfile pricefile' %argv[0])
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)

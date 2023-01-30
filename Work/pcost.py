#!/usr/bin/env python3

# pcost.py
#
# Exercise 1.27
# Exercise 1.30 : Turn code of 1.27 into a funcion
#Exercise 1.32 to use csv lib 
import sys
import csv
import report

def portfolio_cost(filename):
    '''Calculate total cost of portfolio'''
    portfolio = report.read_portfolio(filename)
    return sum([ s.cost for s in portfolio])


def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s potfoliofile' %argv[0])
    filename = argv[1]
    print(f'Total Cost: {portfolio_cost(filename)}')

if __name__ == '__main__':
    import sys
    main(sys.argv)


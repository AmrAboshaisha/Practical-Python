# follow.py

import os
import time

def follow(filename):
    '''Generator function to reads lines being written to end of file'''
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line != '':
                yield line
            else:
                time.sleep(0.1) #sleep breifly


if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
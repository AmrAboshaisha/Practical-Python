from typedproperty import *

class Stock:
    #__slots__ = ('name', 'shares', 'price')
    ''' A stock holding consisting of name, shares and price. '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

    @property
    def cost(self):
        '''Return cost and shares * price'''
        return self.shares * self.price

    def sell(self, nshares):
        '''Sell a number of shares'''
        self.shares -= nshares

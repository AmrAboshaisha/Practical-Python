class Stock:
    __slots__ = ('name', '_shares', 'price')
    ''' A stock holding consisting of name, shares and price. '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

    # Shares getter
    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        '''Return cost and shares * price'''
        return self.shares * self.price

    def sell(self, nshares):
        '''Sell a number of shares'''
        self.shares -= nshares

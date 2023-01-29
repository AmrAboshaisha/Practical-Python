'''
 Focus on the steps that are involved in a creating a table. 
 At the top of the table is a set of table headers. 
 After that, rows of table data appear. 

 This class does nothing, but it serves as a kind of design specification 
 for additional classes that will be defined shortly.
'''

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()




class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output potfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>',end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>') 


def create_formatter(name):
    '''
    Allows a user to create a formatter given an output name 
    such as 'txt', 'csv', or 'html'
    ''' 
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
    return formatter

def print_table(table,columns,formatter):
    '''
    print_table() that prints a table showing user-specified attributes of 
    a list of arbitrary objects. 
    print_table() should also accept a TableFormatter instance to control 
    the output format.

    table : list of stock objects
    columns : list of columns user wants to print
    formatter : a formatter object to print the output

    '''
    formatter.headings(columns)
    for stock in table:
        rowdata = [ str(getattr(stock, colname)) for colname in columns]
        formatter.row(rowdata)

import collections
'''
LC 146 LRU Cache 
LRU (ISBN - > price)cache 
insert 
lookup
erase
'''

class ISBNCache():
    def __init__(self, capacity):
        self.isbn_table = collections.OrderedDict()
        self._capacity= capacity

    def insert(self, isbn, price):
        if isbn in self.isbn_table:
            price = self.isbn_table.pop(isbn)
        elif len(self.isbn_table == self.capacity):
            self.isbn_table.popitem(last=False)   #pop in FIFO, queue like manner
        self.isbn_table[isbn] = price

    def lookup(self, isbn):
        if isbn not in self.isbn_table:
            return -1
        price = self.isbn_table.pop(isbn)
        self.isbn_table[isbn] = price #change the order of the queue
        return price

    def erase(self, isbn):
        return self.isbn_table.pop(isbn, None)


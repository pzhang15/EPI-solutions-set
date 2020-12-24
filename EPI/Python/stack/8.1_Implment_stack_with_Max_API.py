import collections
'''
Design a stack with push(), pop(), and get_max(), 
the get_max() should return the max value int he stack

'''

class Stack_with_Max:
    ElmtWithCachedMax = collections.namedtuple('ElementWithCacheMax',('element', 'max'))
    def __init__(self):
        self.stack_with_max_cache = []
    def empty(self):
        return len(self.stack_with_max_cache) == 0
    def get_max(self):
        return self.stack_with_max_cache[-1].max
    def push(self, x):
        self.stack_with_max_cache.append(
            self.ElmtWithCachedMax(x, x if self.empty() else max(x, self.get_max()))
        )
    def pop(self):
        return self.stack_with_max_cache.pop().element

stack = Stack_with_Max()
data = [2, 1, 6, 5]
for d in data:
    stack.push(d)
while not stack.empty():
    print('max:',  stack.get_max(), 'elmt:', stack.pop())
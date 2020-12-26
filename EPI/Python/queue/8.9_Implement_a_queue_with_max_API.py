import collections
'''
Impomenet a queue with enqueue, dequeue, and getMax
'''
class QueueWithMax:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.max_q = collections.deque()

    def enqueue(self, x: int) -> None:
        self.q.append(x)
        while self.q and self.q[-1] < x: #it will works with duplicates, think about why?
            self.q.pop()
        self.max_q.append(x)        

    def dequeue(self) -> int:
        res = self.q.popleft()
        if self.max_q[0] == res:
            self.max_q.popleft()
        return res

    def max(self):
        return self.max_q[0]
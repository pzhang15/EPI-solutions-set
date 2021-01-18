import collections
class Queue:
    def __init__(self):
        self.q = collections.deque()
        self.max = collections.deque()

    def enqueue(self, x):
        self.q.append(x)
        while self.max and self.max[-1] < x:
            self.max.pop()
        self.max.append(x)

    def dequeue(self):
        res = self.q.popleft()
        if res == self.max[0]:
            self.max.popleft()
        return res

    def getMax(self):
        return self.max[0]
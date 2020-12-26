'''
Given library of stack, implement a queue class
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enq = []
        self.deq = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.enq.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
                
        return self.deq.pop()
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        
        return self.deq[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.deq) + len(self.enq) == 0
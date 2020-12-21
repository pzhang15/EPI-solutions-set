'''
Merge two sorted List, l1, l2 

'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def merge(l1, l2):
    dummy = tail = Node()
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
        


l1 = Node(2)
l1.next = Node(5)
l1.next.next = Node(7)


l2 = Node(3)
l2.next = Node(11)


ret = merge(l1, l2)
p = ret
while(p):
    print(p.data)
    p = p.next


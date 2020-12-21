'''
Given a singly linkedlsit and number k, reorder the list as:
(nodes < k) -> (nodes == k) -> (nodes > k)
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
def sol(l, k):
    less_head = less_itr = Node()
    equal_head = equal_itr = Node()
    greater_head = greater_itr = Node()
    while l:
        if l.data < k:
            less_itr.next = l
            less_itr = less_itr.next

        elif l.data == k:
            equal_itr.next = l
            equal_itr = equal_itr.next
        else:
            greater_itr = l
            greater_itr = greater_itr.next

        l = l.next
    greater_itr.next = None
    less_itr.next = equal_head.next
    equal_itr.next = greater_head.next
    return less_head.next
